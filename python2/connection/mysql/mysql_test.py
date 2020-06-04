#!python3
# coding=utf-8
import pymysql


class mysqlTest():
    def getMysqlInstance(self, host, user, auth, port ):
        con = pymysql.connect(host=host, user=user, password=auth, port=port, charset="utf8")
        return con



if __name__ == '__main__':
    test=mysqlTest()
    con=test.getMysqlInstance("jd_cloud","root","jd123456",3306)
    # cursor=con.cursor()
    # sql='create database if not exists jd_test'
    # cursor.execute(sql)

    cursor=con.cursor()
    sql2="show databases;"
    cursor.execute(sql2)
    data = cursor.fetchall()
    dlist=list(data)
    print(dlist)

    for d in dlist:
        print(type(d))


