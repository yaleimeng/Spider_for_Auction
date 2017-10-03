# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@desc:
@DateTime: Created on 2017/9/9，at 9:50            '''
import pymongo as mg
import time
from string import punctuation

client = mg.MongoClient('localhost',27017)
baoli = client['baoli']    #设定当前操作的数据库。=左边是python变量名，右边中括号里是MongoDB数据库名。
blauc = baoli['NewAuc']     #设定具体操作的数据表。=左边是python用的变量名，右边中括号里面是数据表名。

# index =1
# print(blauc.count())        #打印原先数据库的总数量
# for item in blauc.find():
#     price = item['评估价'].replace(",","")
#     blauc.update({'_id':item['_id']},{'$set':{'评估价':price}})  #每次更新一条数据。
#     print('正在更新第',index,'号数据……')
#     index += 1


#print('数据库更新完成！\n')
#time.sleep(0.5)
out = blauc.find({'成交价':{'$lte':600,'$gt':0}})
for item in out:
    aa = item['评估价']
    print(aa)
print('总共查找出来符合条件的记录：  %d  条。'%(out.count()))


# num = 1
# for itm in querry:
#     dict = {
#                 '名称':itm['名称'],
#                 'LOT号':itm['LOT号'],
#                 '评估价':itm['评估价'].replace(",","") if itm['评估价'] !='无底价' else '无估价',      #把评估价的逗号去掉，防止在csv格式中分为多列。
#                 '成交价':int(itm['成交价'].replace(",","")) if itm['成交价'] !='--' else '--', #把成交价的逗号去掉，转换为数字。便于比较和统计区间
#                 '日期':itm['日期'].replace("-","."),         #把日期格式中的‘-’替换为‘.’，方便日期的比较和计算。
#                 '链接':itm['链接']
#             }
#     if dict not in seen:        #如果字典条目在列表中没出现过
#         seen.append(dict)       #把1条字典保存到列表
#     print('正在处理序号：',num)
#     num +=1
#
# myauc.insert_many(seen)     #把无重复的字典列表插入到数据库的表。
#
# print(myauc.count() )#新建立数据库的总数量。