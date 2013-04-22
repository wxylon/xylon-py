# -*- coding: utf-8 -*-
#coding=utf8
from pymssql import OperationalError
import pymssql
import tool_env2
import sys


class MssqlError(OperationalError): pass

class MSSQ:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        
    def __getConnect(self):
        if not self.db:
            raise MssqlError("异常：")
        try:
            self.conn = pymssql.connect(user=self.user, password=self.passwd, host=self.host, database=self.db, charset="utf-8")
            cur = self.conn.cursor()
            if not cur:
                raise MssqlError("异常：")
            else:
                return cur
        except OperationalError, x:
            #print "异常：" , str(x).decode("gbk").encode("utf-8")
            print "异常：" , tool_env2.force_unicode(str(x))
            sys.exit(0)
    
    def execQuery(self, sql):
        cur = self.__getConnect()
        cur.execute(sql)
        rs = cur.fetchall()
        self.conn.commit()
        self.conn.close()
        return rs
        
def main():
    ms = MSSQ(host="10.10.224.66", user="testwrite1", passwd="test_123_*()", db="couponkpi")
    rs = ms.execQuery("select * from [out_order]")
    for c in rs:
        print c

if __name__ == '__main__':
    main()