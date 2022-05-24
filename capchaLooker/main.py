# #!/usr/bin/python
from __future__ import division
import cv2
from PIL import Image
from matplotlib import pyplot as plt
import urllib
import sys

def pictures_recover(bgImg, slideImg, folder):
    folder = folder + '
    url1 = urllib.urlopen(bgImg)
    with open(folder + 'bgImg.jpeg', 'wb') as f1:
        f1.write(url1.read())
    url2 = urllib.urlopen(slideImg) 
    with open(folder + 'slideImg.png', 'wb') as f2:
        f2.write(url2.read())
        
    bgImg = cv2.imread(folder + 'bgImg.jpeg')  # 背景
    img2 = Image.open(folder + 'slideImg.png') # 拼图块
    xpos = 20
    ypos = 20
    
    region = img2.crop((xpos + 18, ypos + 18, xpos + 76, ypos + 76))
    region.save(folder + 'snapshot2_cut.png') # 从拼图块中获取中心部分（边缘不完整并有羽化，会降低识别率）

    imobj_cut = cv2.imread(folder + 'snapshot2_cut.png')
    template = cv2.imread(folder + 'snapshot2_cut.png', 0)
    w, h = template.shape[::-1]

    result = cv2.matchTemplate(bgImg, imobj_cut, cv2.TM_CCORR_NORMED) # 使用matchTemplate进行模板匹配
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

    top_left = maxLoc # region左上角位置
    bottom_right = (maxLoc[0] + w, maxLoc[1] + h) # region右下角位置

    cv2.rectangle(bgImg, top_left, bottom_right, 255, 2)
    plt.imshow(bgImg, cmap = 'gray')
    plt.title('result'), plt.xticks([]), plt.yticks([])
    plt.savefig(folder + 'match_result.png') # 匹配结果展示
    # plt.show()

    (height, width) = cv2.imread(folder + 'bgImg.jpeg', 0).shape[::-1]
    xtarget_pos = (maxLoc[0] - 36) * (280 / height) # 中心点x轴目标位置

    print(xtarget_pos)
img1 = 'https://hy.captcha.qq.com/hycdn_1_1585565074722004480_0?aid=15000103&asig=&captype=&protocol=https&clientype=2&disturblevel=&apptype=2&curenv=inner&ua=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTRfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcwLjAuMzUzOC43NyBTYWZhcmkvNTM3LjM2&sess=U7j3S48U-OIekKSveV0WD6mThL4BPYm_cedzB3LNCb3tRqB5kVEHj1Pn5RPDcMEN1YxhG0didw5iah5GW9hTHOLk2W9mYlahH0ca5r4njsIqdMBvSwCg5rS8YSBg73hSXi4Y9owtej3FBv8uKNy705RfJrQFzDTbLDZ6ppuxrhw33MkkX16FMd8ImMlo0kODXzX5q_GJ5RQ*&theme=&sid=6620304313193876856&noBorder=noborder&fb=1&forcestyle=undefined&subsid=59&showtype=embed&uid=2649672443&cap_cd=S2Ts2CaasDzL4iLzyDtRyzbhujHk9tju6J2wRD1w1YItt5derEDXgQ**&lang=2052&rnd=927200&TCapIframeLoadTime=29&prehandleLoadTime=64&createIframeStart=1541409714813&rand=0.27157002621020365&websig=7f7f08a3f6405ea7ae5b0e1baa18f5ca7ada87983a1f98bbd254b111bfdedcfed164fca70b2a46a0e199b9cbeab59d67821361bc4e2a8f16fc60185ea632513d&vsig=c01uhgQtas0t41kvIzLVuLvweLW4XTa2CYy5P9R6dE6_miQlTd6nTwqw9_bCohKeUhEbQnW6hZ0DLuqFw9ZBvlaztc4CDlynH2ed-UPoq7qUjsz9NYrKd5dNnUuLcZKENrXsKVmSd__7SfYcMGnZD4cWMmI6KIOKvB4qaYzxGPSyYnIzwuzvIJxhg**&img_index=1'
img2 = 'https://hy.captcha.qq.com/hycdn_2_1585565074722004480_0?aid=15000103&asig=&captype=&protocol=https&clientype=2&disturblevel=&apptype=2&curenv=inner&ua=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTRfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcwLjAuMzUzOC43NyBTYWZhcmkvNTM3LjM2&sess=U7j3S48U-OIekKSveV0WD6mThL4BPYm_cedzB3LNCb3tRqB5kVEHj1Pn5RPDcMEN1YxhG0didw5iah5GW9hTHOLk2W9mYlahH0ca5r4njsIqdMBvSwCg5rS8YSBg73hSXi4Y9owtej3FBv8uKNy705RfJrQFzDTbLDZ6ppuxrhw33MkkX16FMd8ImMlo0kODXzX5q_GJ5RQ*&theme=&sid=6620304313193876856&noBorder=noborder&fb=1&forcestyle=undefined&subsid=60&showtype=embed&uid=2649672443&cap_cd=S2Ts2CaasDzL4iLzyDtRyzbhujHk9tju6J2wRD1w1YItt5derEDXgQ**&lang=2052&rnd=927200&TCapIframeLoadTime=29&prehandleLoadTime=64&createIframeStart=1541409714813&rand=0.27157002621020365&websig=7f7f08a3f6405ea7ae5b0e1baa18f5ca7ada87983a1f98bbd254b111bfdedcfed164fca70b2a46a0e199b9cbeab59d67821361bc4e2a8f16fc60185ea632513d&vsig=c01uhgQtas0t41kvIzLVuLvweLW4XTa2CYy5P9R6dE6_miQlTd6nTwqw9_bCohKeUhEbQnW6hZ0DLuqFw9ZBvlaztc4CDlynH2ed-UPoq7qUjsz9NYrKd5dNnUuLcZKENrXsKVmSd__7SfYcMGnZD4cWMmI6KIOKvB4qaYzxGPSyYnIzwuzvIJxhg**&img_index=2'
# pictures_recover(img1, img2)
pictures_recover(sys.argv[1], sys.argv[2], sys.argv[3])