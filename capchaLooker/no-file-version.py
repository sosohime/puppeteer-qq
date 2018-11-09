# #!/usr/bin/python
from __future__ import division
import cv2
import numpy as np
import urllib
import sys

def url_to_array(url):
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    return image

def pictures_recover(bgImg, slideImg):
    url1 = url_to_array(bgImg)
    url2 = url_to_array(slideImg)

    bgImg = cv2.imdecode(url1, cv2.IMREAD_COLOR)
    
    img2 = cv2.imdecode(url2, cv2.IMREAD_COLOR)
    xpos = 20
    ypos = 20
    
    region = img2[(ypos + 18):(ypos + 76), (xpos + 18):(xpos + 76)]

    result = cv2.matchTemplate(bgImg, region, cv2.TM_CCORR_NORMED)
    maxLoc = cv2.minMaxLoc(result).maxLoc

    top_left = maxLoc
    bottom_right = (maxLoc[0] + w, maxLoc[1] + h)

    width = cv2.imdecode(url1, 0).shape[::-1].width
    xtarget_pos = (maxLoc[0] - 36) * (280 / height)

    print(xtarget_pos)
img1 = 'https://hy.captcha.qq.com/hycdn_1_1585530994156510720_0?aid=15000103&asig=&captype=&protocol=https&clientype=2&disturblevel=&apptype=2&curenv=inner&ua=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTRfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcwLjAuMzUzOC43NyBTYWZhcmkvNTM3LjM2&sess=1wK-j-QHltw8087s_1OLm1t5N6ZM-CcysIvKcfIcVI6xmkylJscmmmBMecWQ78urGMEl0zMsYSzfYB3Ca4-oHWL0hqGWjzI660MR3DY3bPVAo7ESKD2v1Iovy7NTKhiQdevOXVPwn2y6cKXRBxV4vAfWZp4kpTnZbrsvKVdiQgE5Og92JsGnHOpkI_Smo6LG2pne_WQGPys*&theme=&sid=6621308021250973292&noBorder=noborder&fb=1&forcestyle=undefined&subsid=3&showtype=embed&uid=2649672443&cap_cd=AlEV6ycUOTwj-AtqyMZLdJcr9yLm_ZuRkodnayFgqzbvjgHi-vw2Tg**&lang=2052&rnd=406709&TCapIframeLoadTime=115&prehandleLoadTime=70&createIframeStart=1541643408511&rand=0.008890227550662821&websig=9c3ddc65ed4d5c908b74463d88a2c35ecc4fb8cdcb43d61d5bf05b34783bfe285de75f6223b8e6689df5183f41acdbff217ebd2b8590b9045e405c0900d8b4b7&vsig=c01pAYLLLlgR48_QDMYtmuUapF41dS9KGwjlKwtrsTNrHfVil0_yhUovIOSr5-6cA89JBZZsJySkllGJ6uG1iUBtY-KslDPSy551J00ydVxNoaby97iavmqnYcnjRd3Q7QeDaJFVtT5NrX71HYN6JLxZgMWELTFNfbDNv1TabWpuhC6E9EkRqAVgA**&img_index=1'
img2 = 'https://hy.captcha.qq.com/hycdn_2_1585530994156510720_0?aid=15000103&asig=&captype=&protocol=https&clientype=2&disturblevel=&apptype=2&curenv=inner&ua=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTRfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcwLjAuMzUzOC43NyBTYWZhcmkvNTM3LjM2&sess=1wK-j-QHltw8087s_1OLm1t5N6ZM-CcysIvKcfIcVI6xmkylJscmmmBMecWQ78urGMEl0zMsYSzfYB3Ca4-oHWL0hqGWjzI660MR3DY3bPVAo7ESKD2v1Iovy7NTKhiQdevOXVPwn2y6cKXRBxV4vAfWZp4kpTnZbrsvKVdiQgE5Og92JsGnHOpkI_Smo6LG2pne_WQGPys*&theme=&sid=6621308021250973292&noBorder=noborder&fb=1&forcestyle=undefined&subsid=4&showtype=embed&uid=2649672443&cap_cd=AlEV6ycUOTwj-AtqyMZLdJcr9yLm_ZuRkodnayFgqzbvjgHi-vw2Tg**&lang=2052&rnd=406709&TCapIframeLoadTime=115&prehandleLoadTime=70&createIframeStart=1541643408511&rand=0.008890227550662821&websig=9c3ddc65ed4d5c908b74463d88a2c35ecc4fb8cdcb43d61d5bf05b34783bfe285de75f6223b8e6689df5183f41acdbff217ebd2b8590b9045e405c0900d8b4b7&vsig=c01pAYLLLlgR48_QDMYtmuUapF41dS9KGwjlKwtrsTNrHfVil0_yhUovIOSr5-6cA89JBZZsJySkllGJ6uG1iUBtY-KslDPSy551J00ydVxNoaby97iavmqnYcnjRd3Q7QeDaJFVtT5NrX71HYN6JLxZgMWELTFNfbDNv1TabWpuhC6E9EkRqAVgA**&img_index=2'
pictures_recover(img1, img2)
# pictures_recover(sys.argv[1], sys.argv[2])