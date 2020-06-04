#!python3
# coding=utf-8
import pymysql
import logging

class mysqlTest():
    logging.basicConfig(level="INFO")
    def getMysqlInstance(self, host, user, auth, port, dbname):
        con = pymysql.connect(host=host, user=user, password=auth, port=port, database=dbname, charset="utf8")
        return con

    def createTable(self, tableName, dbName, cursor):
        sql = """
    CREATE TABLE jojo_test (
    id INT auto_increment PRIMARY KEY ,
    name CHAR(10) NOT NULL UNIQUE,
    age TINYINT NOT NULL
    )ENGINE=innodb DEFAULT CHARSET=utf8;
    """
        cursor.execute(sql)

    ## 插入记录
    def insetData(self, name, age, cursor):
        sql = "insert into jojo_test (name,age) values (%s,%s)";
        cursor.execute(sql, [name, age])
    ## 修改记录
    def updateData(self,name,age,cursor):
        sql="update jojo_test set age=%s where name= %s"
        cursor.execute(sql,[age,name])
    ##删除记录
    def deleteData(self,name,cursor):
        sql="delete from jojo_test where name=%s"
        cursor.execute(sql,[name])
    ##查询多条记录
    def queryManyRecords(self,cursor):
        sql="select * from jojo_test"
        cursor.execute(sql)
        data=cursor.fetchmany(2)
        dlist=list(data)
        return dlist

if __name__ == '__main__':
    test = mysqlTest()
    con = test.getMysqlInstance("jd_cloud", "root", "jd123456", 3306, dbname="jd_test")
    cursor = con.cursor()
    # sql='create database if not exists jd_test'
    # cursor.execute(sql)
    ## get cursor
    # test.createTable('test', '', cursor)
    name = 'ken'  # type: str
    # test.deleteData(name,cursor)
    dlist=test.queryManyRecords(cursor)
    print(str(dlist))
    con.commit()
    # logging.info("infos were update successed ! ")
    # logging.info("infos were delete successed ! ")

    logging.info("more info are query successed!")


