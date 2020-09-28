#!python3
# coding=utf-8
from elasticsearch import Elasticsearch


class es_util(object):

    ##创建连接
    def getEsConnect(self, host, port):
        hosts = []
        hosts.append('{}:{}'.format(host, port))
        es = Elasticsearch(hosts)
        return es

    ##搜索
    def search(self, es, index, body):
        response = es.search(
            index=index,
            body=body
        )
        return response