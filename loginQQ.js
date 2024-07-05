const path = require('path');
const { spawnSync } = require('child_process');
const puppeteer = require('puppeteer');

const account = {
    qq: process.env.qq_account
    pwd: process.env.qq_pwd
}

let timeout = function (delay) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            try {
                resolve(1)
            } catch (e) {
                reject(0)
            }
        }, delay);
    })
}

let page = null
let captchaFrame = null
let btn_position = null
let initDistance = 0
let slideLink = null;
let times = 0 // 执行重新滑动的次数
const distanceError = [-10, 2, 3, 5] // 距离误差

async function loginQQ(qq, pwd) {
    const browser = await puppeteer.launch({
        headless: false, // 打开浏览器
        defaultViewport: {
            width: 1200,
            height: 800
        }
    });
    page = await browser.newPage();

    // 1.打开qq登陆页
    // await page.goto('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=15000103&s_url=http%3A%2F%2Fe.qq.com%2F');
    await page.goto('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=716027609&daid=383&style=33&login_text=授权并登录&hide_title_bar=1&hide_border=1&target=self&s_url=http%3A%2F%2Fe.qq.com%2F')
    await timeout(1000);

    // 2.打开登录页面
    page.click('#switcher_plogin')
    await timeout(1000);

    // 3.输入账号密码
    page.type('#u', account.qq)
    await timeout(500);
    page.type('#p', account.pwd)
    await timeout(1000);

    // 4.点击登陆
    page.click('#login_button')
    await timeout(4000);

    // 如果没触发滑动验证码直接跳过下面的步骤
    if(page.url().indexOf('xui.ptlogin2.qq.com') < 0) {
        console.log('login success')
        return page
    }

    // 获取iframe
    captchaFrame = await getActiveIFrame();

    // 获取滑块位置
    btn_position = await getBtnPosition();

    // 5.滑动
    drag(null)
}

async function getActiveIFrame() {
    const frame = await page.mainFrame().childFrames()[0]
    return frame
}

// py进行差异对比计算距离
async function getDistance() {
    const imgs = await captchaFrame.evaluate(() => {
        const bgUrl = document.querySelector('#slideBkg').src;
        const slideUrl = document.querySelector('#slideBlock').src;
        return {bgUrl, slideUrl}
    })
    slideLink = imgs.slideUrl
    const folderPath = path.resolve(__dirname, 'capchaLooker')
    const pyprog = spawnSync('python', [path.resolve(folderPath, 'main.py'), imgs.bgUrl, imgs.slideUrl, folderPath])
    const centerPos = pyprog.stdout.toString('utf8');

    return {
        min: centerPos - 12 - 2,
        max: centerPos - 12 + 1
    }
}

// 获取滑块位置
async function getBtnPosition() {
    const btn_position = await page.evaluate(() => {
        const {
            offsetTop,
            offsetLeft
        } = document.querySelector('#newVcodeIframe')
        return {
            btn_left: offsetLeft + 30,
            btn_top: offsetTop + 220
        }
    })
    return btn_position;
}

// 尝试滑动
async function tryValidation(distance) {
    //将距离拆分成三段，模拟正常人的行为
    const distance1 = 20
    const distance2 = distance - 10 - 20
    const distance3 = 10

    // 按下
    page.mouse.down(btn_position.btn_left, btn_position.btn_top)

    // 起始段
    page.mouse.move(btn_position.btn_left + distance1, btn_position.btn_top, {
        steps: 17
    })
    await timeout(400);
    // 加速段
    page.mouse.move(btn_position.btn_left + distance1 + distance2, btn_position.btn_top, {
        steps: 20
    })
    await timeout(800);
    // 减速段
    page.mouse.move(btn_position.btn_left + distance1 + distance2 + distance3, btn_position.btn_top, {
        steps: 15
    })
    await timeout(1200);
    page.mouse.up()
    page.mouse.move(btn_position.btn_left, btn_position.btn_top, {
        steps: 25
    })
    await timeout(100);

    captchaFrame = await getActiveIFrame();

    const isSuccess = await captchaFrame.evaluate(() => {
        return document.querySelector('#tcaptcha_cover_success') && document.querySelector('#tcaptcha_cover_success').innerHTML
    })
    const reDistance = await captchaFrame.evaluate(() => {
        return document.querySelector('.tcaptcha-title') && document.querySelector('.tcaptcha-title').innerHTML
    })
    const slideLinkNow = await captchaFrame.evaluate(() => {
        return  document.querySelector('#slideBlock').src;
    })

    return {
        isSuccess: isSuccess.includes('s'),
        reDistance: reDistance.includes('有点难') || slideLinkNow != slideLink
    }
}

async function drag(distance) {
    distance = distance || await getDistance();
    const result = await tryValidation(distance.min)
    if (result.isSuccess) {
        await timeout(1000);
        //登录
        console.log('验证成功')
        return page;
    } else if (result.reDistance) {
        console.log('重新滑动')
        times = 0
        await drag(null)
    } else {
        if (distanceError[times]) {
            times++
            console.log('重新滑动')
            await drag({
                min: distance.max,
                max: distance.max + distanceError[times]
            })
        } else {
            console.log(distanceError.length + '次滑动失败，程序退出')
            loginQQ()
            // process.exit()
        }
    }
}

loginQQ()
