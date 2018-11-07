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
    w, h = region.shape[:-1]

    result = cv2.matchTemplate(bgImg, region, cv2.TM_CCORR_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

    top_left = maxLoc
    bottom_right = (maxLoc[0] + w, maxLoc[1] + h)

    (height, width) = cv2.imdecode(url1, 0).shape[::-1]
    xtarget_pos = (maxLoc[0] - 36) * (280 / height)

    print(xtarget_pos)
img1 = 'https://hy.captcha.qq.com/hycdn_1_1585378161671326464_0?aid=15000103&asig=&captype=&protocol=https&clientype=2&disturblevel=&apptype=2&curenv=inner&ua=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTRfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcwLjAuMzUzOC43NyBTYWZhcmkvNTM3LjM2&sess=qykoTUsezV3FsUHEW8Rj7-Z-CsNfMPbycQPlqya2aQPNp7fT4ej0AbSOyILX8dKF9j6ELoDUTeZ3wV6mxWClS3ZVTlYeXoWndsFr40LURuOjvXEOKxZgfLME8kmjrY9siKziLThUwCfR4pEo9pHOcwntYw9nF8J87_NwN4XPESjODgLsbwqW5AT3ifNk7HILuNVcF8uF32A*&theme=&sid=6620937511706284631&noBorder=noborder&fb=1&forcestyle=undefined&subsid=3&showtype=embed&uid=2649672443&cap_cd=st0OnHQrjEKL3g8ymhy4wxIwP-wroTfrqVRH_Wc2HLU9Ynqk5QJxMw**&lang=2052&rnd=412991&TCapIframeLoadTime=92&prehandleLoadTime=69&createIframeStart=1541557142048&rand=0.9931651561218753&websig=af84efa050a5af30d6cc257cfc5a374c22aff27bc00a97aa8232fe7a413cd12e8dc5af109565294ff27339f2d67a7548b95b969a2a8927c03189d94f182011bf&vsig=c01TZEEmrfnN2lX56g0Zk-kpkeRn37PkCDU2roLDXufdoZFqYnVxYsofi29XhBpE1iXjzUFMvKHcNXAO8GIixENvxgjLc_S4vJ75-WVn61wborxp_zXBmnqpr1XZaaR9cYB3g92n4GJu-WPp0WVDmlaKOGeSpNgAumtCItupRjx45nHrnvaWCVAxg**&img_index=1'
img2 = 'https://hy.captcha.qq.com/hycdn_2_1585378161671326464_0?aid=15000103&asig=&captype=&protocol=https&clientype=2&disturblevel=&apptype=2&curenv=inner&ua=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTRfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcwLjAuMzUzOC43NyBTYWZhcmkvNTM3LjM2&sess=qykoTUsezV3FsUHEW8Rj7-Z-CsNfMPbycQPlqya2aQPNp7fT4ej0AbSOyILX8dKF9j6ELoDUTeZ3wV6mxWClS3ZVTlYeXoWndsFr40LURuOjvXEOKxZgfLME8kmjrY9siKziLThUwCfR4pEo9pHOcwntYw9nF8J87_NwN4XPESjODgLsbwqW5AT3ifNk7HILuNVcF8uF32A*&theme=&sid=6620937511706284631&noBorder=noborder&fb=1&forcestyle=undefined&subsid=4&showtype=embed&uid=2649672443&cap_cd=st0OnHQrjEKL3g8ymhy4wxIwP-wroTfrqVRH_Wc2HLU9Ynqk5QJxMw**&lang=2052&rnd=412991&TCapIframeLoadTime=92&prehandleLoadTime=69&createIframeStart=1541557142048&rand=0.9931651561218753&websig=af84efa050a5af30d6cc257cfc5a374c22aff27bc00a97aa8232fe7a413cd12e8dc5af109565294ff27339f2d67a7548b95b969a2a8927c03189d94f182011bf&vsig=c01TZEEmrfnN2lX56g0Zk-kpkeRn37PkCDU2roLDXufdoZFqYnVxYsofi29XhBpE1iXjzUFMvKHcNXAO8GIixENvxgjLc_S4vJ75-WVn61wborxp_zXBmnqpr1XZaaR9cYB3g92n4GJu-WPp0WVDmlaKOGeSpNgAumtCItupRjx45nHrnvaWCVAxg**&img_index=2'
pictures_recover(img1, img2)
# pictures_recover(sys.argv[1], sys.argv[2])