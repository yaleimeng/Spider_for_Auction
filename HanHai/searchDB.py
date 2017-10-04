# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@desc:
@DateTime: Created on 2017/9/9，at 9:50            '''
import pymongo as mg
import time
client = mg.MongoClient('localhost',27017)
hanhai = client['Hanhai']    #设定当前操作的数据库。=左边是python变量名，右边中括号里是MongoDB数据库名。
hhauc = hanhai['hhAuc']      #设定具体操作的数据表。=左边是python用的变量名，右边中括号里面是数据表名。

print('数据库条目总数：',hhauc.count())

# index =1
# for item in hhauc.find({'6': {'$exists': True}}):                   #更新带有字段6的条目
#     hhauc.update({'_id':item['_id']},{'$unset':{'6':item['6'] }})   #每次更新一条数据。删除6这个字段。
#     print('已经更新',index,'条数据……')
#     index += 1
#
# print('数据库更新完成！\n')
# time.sleep(0.8)
out  = hhauc.find({'成交价': {'$lt': 500000}})  # 带有名字叫6的字段的条目。
# for item in out:
#     print(item)

print('查询结果数量：',out.count())


#hhauc.update({'6': {'$exists': True}},{"$set":{"成交价":'$6'}})   #给带有6字段的条目增加新的字段，成交价

# index =1
# print(blauc.count())        #打印原先数据库的总数量
# for item in blauc.find():
#     price = item['评估价'].replace(",","")
#     blauc.update({'_id':item['_id']},{'$set':{'评估价':price}})  #每次更新一条数据。
#     print('正在更新第',index,'号数据……')
#     index += 1


#print('数据库更新完成！\n')
#time.sleep(0.5)
# out = hhauc.find({'成交价':{'$lte':600,'$gt':0}})
# for item in out:
#     aa = item['评估价']
#     print(aa)
# print('总共查找出来符合条件的记录：  %d  条。'%(out.count()))
