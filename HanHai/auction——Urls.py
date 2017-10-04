# # -*- coding: utf-8 -*-
# '''
# @author: Yalei Meng    E-mail: yaleimeng@sina.com
# @license: (C) Copyright 2017, HUST Corporation Limited.
# @desc:
# @DateTime: Created on 2017/9/8，at 15:38            '''
# from bs4 import BeautifulSoup as bs
# import requests as  rq
# import pymongo as mg
# import time
# import random
#
# def  get_session_from(top):
#     r = rq.get(top)
#     soup = bs(r.text, 'lxml')
#      # 在页面中找到拍卖专场，的位置
#     arts = soup.select('div.Auction-results > div > ul > li > div > div > a')
#     with open('E:/Hanhai_List_URLs.txt', 'a', encoding='utf-8')as f:
#         for bk in arts:
#             link = host + bk.get('href')
#             out.append(link)
#             f.write(link)
#             f.write("\n")
#             print(link)
#
#
# out = []
# host = 'http://www.hanhai.net'
# urls = ['http://www.hanhai.net/Auction-results-meet.php?s=0&page={}'.format(str(n)) for n in range(0,114)] #不含114
#
# #get_session_from(urls[21])
#
# for u in urls:
#     get_session_from(u)
#     print('目前已写入 %d个链接。！' % len(out))
#     time.sleep(random.uniform(0.7,2.1))
#
# print('\n全部链接写入完成！\n程序结束！')