#!/usr/local/bin/python

import redis

r= redis.StrictRedis(host='localhost',port=6379,db=0)
keys = r.keys()
dict1 = {}
for i in keys:
     a = i.decode('utf-8') 
     b = r.get(i).decode('utf-8')
     dict2 = {a:int(b)}
     dict1.update(dict2)
print(dict1)
 
