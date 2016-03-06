#coding:utf-8
import sys
import MySQLdb

class TransferMoney():
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, src, target, money):
        try:
            self.check_acct_available(src)
            self.check_acct_available(target)
            self.has_enough_money(src, money)
            self.reduce_money(src, money)
            self.add_money(target, money)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()

    def reduce_money(self, src, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money - %s where acctid = %s" %(money, src)
            cursor.execute(sql)
            print "reduce_money: " + sql
            #rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("the account reduce money fail")
        finally:
            cursor.close()


    def add_money(self, target, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money + %s where acctid = %s" %(money, target)
            cursor.execute(sql)
            print "add_money: " + sql
            #rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("the account add money fail")
        finally:
            cursor.close()


    def check_acct_available(self, accit):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid =  %s" %accit
            cursor.execute(sql)
            print "check_acct_available: " + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("the account %s is not exist" %accit)
        finally:
            cursor.close()

    def has_enough_money(self, src, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid =  %s and money >= %s " %(src, money)
            cursor.execute(sql)
            print "has_enough_money: " + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("the account does not have enough money")
        finally:
            cursor.close()


if __name__ == "__main__":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    conn = MySQLdb.connect(
        host = "127.0.0.1", user = 'root', passwd = '111111', port = 3306, db = 'cotyb'
    )
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print e
    finally:
        conn.close()