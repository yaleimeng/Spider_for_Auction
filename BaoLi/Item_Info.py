# # -*- coding: utf-8 -*-
# '''
# @author: Yalei Meng    E-mail: yaleimeng@sina.com
# @license: (C) Copyright 2017, HUST Corporation Limited.
# @desc:
# @DateTime: Created on 2017/9/7，at 18:18            '''
# from bs4 import BeautifulSoup as bs
# import requests as  rq
# import pymongo as mg
# import time
# import random
# from multiprocessing import Pool
#
# def  get_items_from(page):
#     global  count,newURLs,oldURLs
#     um = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36'
#     ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36'
#     up = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Mobile Safari/537.36'
#     head = {'User-Agent': ua}
#     host = 'http://www.polypm.com.cn/'
#     r = rq.get(page,headers = head)
#     time.sleep(random.uniform(1.0,2.5))
#     soup = bs(r.text, 'lxml')
#     items = soup.select('strong > a')
#     infos = soup.select('div.work_txt > p')
#     for itm,inf in zip(items,infos):
#         dict = {
#             '名称':itm.text,         #正确
#             'LOT号':inf.text.split("\n\n")[0][6:],   #获取正确。
#             '评估价':inf.text.split("\n\n")[1].replace(' ','')[3:],
#             '成交价':inf.text.split("\n\n")[2].replace('\n ','').replace(' ','')[7:],
#             '日期':inf.text.split("\n\n")[3][5:],
#             '链接':host+itm['href']
#         }
#         #print (dict)
#         count += 1
#         blauc.insert_one(dict)    #也可以考虑把词典列表一次性写入到数据库。【暂时先不写数据库。】
#
#     # 在页面中找到底部页码的位置
#     new_urls = soup.find('div',class_='page').find_all('a')
#     for one in new_urls:        #第一步抓取底部的url，比对是否已在newURL内，如果不在，则加入到newURL列表。
#         part = one.get('href')  #尝试获得某属性。。如果中括号就是直接访问某属性，如果不存在会崩溃。
#         if part is not None :
#             full = host + part
#             if full not in newURLs:
#                 newURLs.add(full)
#                 print('发现新页面：'+full)           # 打印新获取的页码对应url
#                 get_items_from(full)  # 如果新的旧的都没有，则递归调用自身。
#
# client = mg.MongoClient('localhost',27017)
# baoli = client['baoli']    #设定当前操作的数据库。=左边是python变量名，右边中括号里是MongoDB数据库名。
# blauc = baoli['NewAuc']     #设定具体操作的数据表。=左边是python用的变量名，右边中括号里面是数据表名。
#
# newURLs = set()
# urls = []                                 #这是所有专场的url地址。
# with open('E:/Auction_List_URLs.txt', 'r', encoding='utf-8')as f:
#     for line in f.readlines():         #按整行依次读取数据。
#         link = line.replace("\n",'')   #把回车符号替换为空。这样网址就是可访问的。
#         urls.append(link)
#
# count =0;       num = 773     #num是——【开始数字】！！
# print('列表中母链接总数为%d。'%len(urls))
#
# for one in range(num,len(urls)):
#     real = urls[one][:-3]+'order//order_sc//np/0'  #真实地址。
#     newURLs.add(real)
#     print('正在获取第\t%d\t场拍卖会详情：'%num)
#     get_items_from(real)    # 从测试会场获取这个会场，几页里面所有物品的信息。
#     print('根据第\t%d\t母链接，共收集了%d条藏品信息。' % (num,count))
#     print('当前数据库中物品总数：',blauc.count())
#     count = 0;      num += 1
#     #time.sleep(random.uniform(0.8,1.6))
#
# # if __name__ == '__main__':
# #     pool = Pool()                      #开启多个进程。
# #     pool.map(get_all_items,all)      #从构造好的链接列表all中依次取出,分别执行get_all_items函数。