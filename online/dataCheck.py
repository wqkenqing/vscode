#!python3
# coding=utf-8

## check the result
import redis
from elasticsearch import Elasticsearch
import json

class dataCheck(object):
    ## 获取redis连接
    def getRedisConnection(self, host, port, auth):
        pool = redis.ConnectionPool(host=host, port=port, db=0, password=auth, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        return r

    def getEsConnect(self, host, port):
        connect = []
        connect.append("{}:{}".format(host, port))
        es = Elasticsearch(connect)
        return es

    def getLocalRedisConnect(self):
        host = "192.168.10.101"
        port = "6379"
        auth = "test123"
        return self.getRedisConnection(host, port, auth)

    def getCountTotalFromLocalRedis(self):
        r = check.getLocalRedisConnect()
        total = r.hgetall("LYDSJ_GATHER_LOG_COUNT_TOTAL")
        return total

    def getCountInfoFromLocalEs(self, host, port):
        host = "namenode2"
        port = "9200"
        es = self.getEsConnect(host, port)
        return self.getIndexCount(es.cat.indices())

    def getIndexStore(self, content):
        cons = content.split("\n")
        dict = {}
        for row in cons:
            rows = row.split(" ")
            if (len(rows) > 2):
                dict.__setitem__(rows[2], rows[7])
        return dict

    def getIndexCount(self, content):
        cons = content.split("\n")
        dict = {}
        for row in cons:
            rows = row.split()
            if (len(rows) > 2):
                dict.__setitem__(rows[2], rows[6])
        return dict

    def writeesRowIntoLocal(self):
        outpath1 = "/Users/wqkenqing/Desktop/tmpdoc/es_count.txt"
        res = self.getCountInfoFromLocalEs("", "")
        f = open(outpath1, "w")
        for k, v in res.items():
            row = "{} {}".format(k, v)
            f.write(row)
            f.write("\n")

        f.close()

    def writeRedisRowIntoLocal(self):
        outpath2 = "/Users/wqkenqing/Desktop/tmpdoc/redis_store.txt"
        res = self.getCountTotalFromLocalRedis()
        f = open(outpath2, "w")
        for k, v in res.items():
            row = "{} {}".format(k, v)
            f.write(row)
            f.write("\n")
        f.close()


if __name__ == '__main__':
    check = dataCheck()
    # check.writeRedisRowIntoLocal()
    check.writeesRowIntoLocal()
    # es=check.getLocalRedisConnect()
    # print(es.cat.indices())
    # res=check.getEsConnect("namenode2","9200")
    # print(res.cat.indices())



