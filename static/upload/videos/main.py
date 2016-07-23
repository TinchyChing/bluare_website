import urllib.request
import re
import sys
import os 
import socket

targetDir = "/Users/Tinchy/工作室/image"
def crawler(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    matchOBJ = re.findall(r'"thumbURL":"(.*?)"',data)
    for i in matchOBJ:
        print(i)
        urllib.request.urlretrieve(i, targetDir) 
    else:
        print ("all")
url = "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1467293618228_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%91%84%E5%BD%B1"
crawler(url)
