#!python3
# coding=utf-8
import  redis

## redis连接
class redisTest():

    def getRedisInstance(self,host,port,auth):
        pool=redis.ConnectionPool(host=host,port=port,db=0,password=auth)
        r = redis.Redis(connection_pool=pool,encoding="utf8")
        return r

    def getRedisInstanceByStrictRedis(self,host,port,auth):
        ## 注意decode解码,不然获取的数据是byte类型

        r=redis.StrictRedis(host=host,port=port,db=0,password=auth,decode_responses=True)
        return r




if __name__ == '__main__':
    test=redisTest()
    r=test.getRedisInstanceByStrictRedis(host='jd_cloud',port=6380,auth='test123')
    ## 获取keys
    klist=r.keys()

    ## 添加value
    # r.set("name_key","joe")
    ## 获取name_key's value
    val=r.get("name_key")
    print(val)





