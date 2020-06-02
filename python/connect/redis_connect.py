#!python
#--*-- encoding:utf8 --*--

import redis
import time



# pool = redis.ConnectionPool(host='jd_cloud', port=6379, decode_responses=True)

pool =redis.ConnectionPool(host='jd_cloud', port=6380, db=0, password='test123')

# print(dir(redis.Redis))
# r = StrictRedis(connection_pool=pool)
r = redis.Redis(connection_pool=pool)
# r=redis.StrictRedis(host='jd_cloud',port=6379,password='test123',decode_responses=True,db=0)
# r.hset("hash1","k1","k2")

print(r.hget("hash1","k1"))
