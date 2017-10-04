# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@desc:
@DateTime: Created on 2017/9/9，at 11:18            '''
from bs4 import BeautifulSoup as bs
import requests as  rq
import pymongo as mg
import time
import random

def  get_items_from(page):
    global  count,newURLs,oldURLs,head,host
    r = rq.get(page,headers = head, timeout=10)
    time.sleep(random.uniform(1.2,2.5))         #访问间隔时间。
    soup = bs(r.content, 'lxml')                #因为文字编码问题，不能使用text，而必须是content
    items = soup.select('ul.dataItem2 > h4 > a')
    infos = soup.select('ul.dataItem2')
    for itm,inf in zip(items,infos):
        str_list = inf.find_all('li')
        dict = {
            '名称':itm.text,                 #正确
            'LOT号' :str_list[0].text[6:],   #获取正确。
            '评估价':str_list[1].text.replace(',','').replace('\n','').replace(' ','')[6:],
            '成交价':'--' if str_list[2].text.split('：')[1] =='--' else str_list[2].text.split('：')[1][4:],
            '日期'  :str_list[3].text[3:],
            '链接'  :host+itm['href']        }
        count += 1
        #print (dict)          #调试时可以打印字典出来观察。
        Dic_list.append(dict)
    #if len(Dic_list)>0:
        #print('—'*12,Dic_list[-1]['名称'])  # 调试时可以打印字典出来观察。


    new_urls = soup.select('div.page > span')   # 在页面中找到底部页码的位置
    if len(new_urls)>2:                     #如果页面上存在页码的连接，才进行寻找，否则跳过。
        links = new_urls[2].find_all('a')
        for link in links:                  #第一步抓取底部的url，
           full = host +  link.get('href')
           if full not in newURLs:          #比对是否已在newURL内，如果不在，则加入到newURL列表。
               newURLs.add(full)
               print('发现新页面：'+full)   # 打印新获取的页码对应url
               get_items_from(full)         #如果属于全新链接，则递归调用自身。

client = mg.MongoClient('localhost',27017)
hanhai = client['Hanhai']    #设定当前操作的数据库。=左边是python变量名，右边中括号里是MongoDB数据库名。
hhauc = hanhai['hhAuc']     #设定具体操作的数据表。=左边是python用的变量名，右边中括号里面是数据表名。
ug = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36'
ua ='Mozilla/5.0 (Windows NT 6.1;) AppleWebKit/532.5 (KHTML, like Gecko) Safari/532.5'
uk = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36'
head = {'User-Agent': ua}
host = 'http://www.hanhai.net/'
newURLs = set();            Dic_list=[]
urls = []                                 #这是所有专场的url地址。
with open('E:/Hanhai_List_URLs.txt', 'r', encoding='utf-8')as f:
    for line in f.readlines():         #按整行依次读取数据。
        link = line.replace("\n",'')   #把回车符号替换为空。这样网址就是可访问的。
        urls.append(link)

count =0;       num = 560      #num是——【开始数字】！！记录当前访问场次的。
#count记录的是每个链接进去递归访问之后，藏品的总数。
if __name__ =='__main__':
    for one in range(num,837):
        real = urls[one][:-14]+'&s=0&aucpage=1'  #格式调整，与批量访问的地址保持一致。
        newURLs.add(real)
        print('\n获取第\t%d  场拍卖会详情：'%num,real)
        get_items_from(real)                 # 从种子链接获取这个会场，全部页码里面所有物品的信息。
        if len(Dic_list)>0:
            hhauc.insert_many(Dic_list)          #一次性把字典列表写入数据库。这样如果函数失败，就不会写入。避免了重复。
            Dic_list.clear()                     #用完后清空字典。
        print('根据第\t%d\t条种子，共收集了 %d 条藏品信息。' % (num,count),'当前数据库中物品总数：',hhauc.count())
        count = 0;          newURLs.clear();            num += 1