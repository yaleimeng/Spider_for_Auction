# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@desc:
@DateTime: Created on 2017/9/7，at 17:48            '''
from bs4 import BeautifulSoup as bs
import requests as  rq
import pymongo as mg
import time
import random

def  get_session_from(top):
    r = rq.get(top)
    soup = bs(r.text, 'lxml')
     # 在页面中找到拍卖专场，的位置
    books = soup.select('strong > a')
    with open('E:/Auction_List_URLs.txt', 'a', encoding='utf-8')as f:
        for bk in books:
            link = host + bk['href']
            out.append(link)
            f.write(link)
            f.write("\n")
            print(link)


out = []
host = 'http://www.polypm.com.cn/'
urls = ['http://www.polypm.com.cn/index.php?s=Auction/index/tp/0/np/{}'.format(str(n)) for n in range(0,75)] #不含75

for u in urls:
    get_session_from(u)
    time.sleep(random.uniform(1.5,3))

print('所有 %d个链接写入完成！\n程序结束！'%len(out))