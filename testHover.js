const path = require('path');
const {
    spawnSync
} = require('child_process');
const puppeteer = require('puppeteer');

const account = require('./accounts');

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

function getElementLeft(element) {
    var actualLeft = element.offsetLeft;
    var current = element.offsetParent;

    while (current !== null) {
        actualLeft += current.offsetLeft;
        current = current.offsetParent;
    }

    return actualLeft;
}

function getElementTop(element) {
    var actualTop = element.offsetTop;
    var current = element.offsetParent;

    while (current !== null) {
        actualTop += current.offsetTop;
        current = current.offsetParent;
    }

    return actualTop;
}


async function go() {
    const browser = await puppeteer.launch({
        headless: false, // 打开浏览器
        defaultViewport: {
            width: 1200,
            height: 800
        }
    });
    page = await browser.newPage();

    // 1.打开qq登陆页
    await page.goto('https://www.json.cn/');
    await timeout(3000);

    const position = await page.evaluate(() => {
        const btn = document.querySelector('.tip.zip');

        function getElementLeft(element) {
            var actualLeft = element.offsetLeft;
            var current = element.offsetParent;

            while (current !== null) {
                actualLeft += current.offsetLeft;
                current = current.offsetParent;
            }

            return actualLeft;
        }

        function getElementTop(element) {
            var actualTop = element.offsetTop;
            var current = element.offsetParent;

            while (current !== null) {
                actualTop += current.offsetTop;
                current = current.offsetParent;
            }

            return actualTop;
        }
        return {
            left: getElementLeft(btn),
            top: getElementTop(btn),
        }
    })

    console.log(position, '--------------------')

    await page.mouse.move(position.left, position.top);

    const hoverText = await page.evaluate(() => {
        return document.querySelector('.tooltip-inner').innerText
    })

    console.log(hoverText)
}

go()