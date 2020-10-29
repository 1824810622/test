import pymysql
#创建连接

class DBoperation:

    def __init__(self):
        self.conn = pymysql.Connection(host='localhost', user='root', password='123456', database='crm', port=3306,
                                  charset='utf8')
        self.cur=self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def search_all(self,sql):
#创建游标cursor=pymysql.cursors.DictCursor
        try:
#执行sql
            self.cur.execute(sql)
            res = self.cur.fetchall()
            print(res)

        except Exception as e:
            print(e)
#游标fetchall方法获取数据


    def update(self,sql):

        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('ok')
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()

    def delet(self,sql):
        try:
            # sql:
            # 执行sql
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        # else:
        #     print('operation success~')
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()

    def add(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.cur.close()
            self.conn.close()








# dbopration=DBoperation()
# dbopration.search_all('select * from customer_info where customer_job="老板";')
# dbopration.update('update customer_info set customer_job="freeman" where customer_tel="54545433";')
# dbopration.delet("delete from customer_info where customer_name='gigi';")
# dbopration.add('insert into customer_info(customer_name) values("anny")')