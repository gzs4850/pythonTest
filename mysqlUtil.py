#  -*- coding: utf-8 -*-
from pymysql import connect

class MysqlHelp(object):
    # 初始化方法
    def __init__(self, database, host='192.168.18.2', user='root', password='root', charset='utf8', port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port

    # 初始化完后连接到数据库并创建好游标
    def open(self):
        # 连接数据库
        self.conn = connect(host=self.host, user=self.user, password=self.password, database=self.database,
                            charset=self.charset, port=self.port)
        # 创建游标
        self.cur = self.conn.cursor()

    # 关闭数据库
    def close(self):
        self.cur.close()
        self.conn.close()

    # 增删改
    def sql_execute(self, sql, L=[]):
        self.open()
        # 对sql语句处理
        try:
            self.cur.execute(sql, L)  # 执行sql命令
            self.conn.commit()  # 提交到数据库执行
            # print('ok')
        except Exception as e:
            self.conn.rollback()
            print('failed', e)
        self.close()

    # 查询所有
    def getAll(self, sql, L=[]):
        self.open()
        self.cur.execute(sql, L)
        result = self.cur.fetchall()  # 查询结果用result绑定
        self.close()
        return result  # 将查询到的结果返回回去

    # 查询一条
    def getOne(self, sql, L=[]):
        self.open()
        self.cur.execute(sql, L)
        result = self.cur.fetchone()  # 查询结果用result绑定
        self.close()
        return result  # 将查询到的结果返回回去

def insertIDCard():
    import genIDCard,time
    IDCard = genIDCard.gen_id_card()
    # print(IDCard)
    mysql = MysqlHelp('fastrunner')
    sql_insert = 'insert into t_avl_idcard_no(cardNo, status, TIMESTAMP, useage) values(%s, %s, %s, %s);'
    mysql.sql_execute(sql_insert, [IDCard, '0',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),''])

def insertPhoneNo(i):
    import genIDCard,time
    phoneNo = genIDCard.gen_phoneNo(i)
    # print(phoneNo)
    mysql = MysqlHelp('fastrunner')
    sql_insert = 'insert into t_avl_phone_no(phoneNo, status, TIMESTAMP, useage) values(%s, %s, %s, %s);'
    mysql.sql_execute(sql_insert, [phoneNo, '0',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),''])

def getAllIDCard():
    # 创建一个实例对象，把数据库传进去
    mysql = MysqlHelp('fastrunner')
    sql_select = 'select * from t_avl_idcard_no;'
    result = mysql.getAll(sql_select)  # 返回一个元组
    for i in result:
        print(i)

def delIDCard(cardNo):
    mysql = MysqlHelp('fastrunner')
    sql_delete = 'delete from t_avl_idcard_no where cardNo=%s'
    mysql.sql_execute(sql_delete, cardNo)

def getIDCard():
    # 创建一个实例对象，把数据库传进去
    mysql = MysqlHelp('fastrunner')
    sql_select = 'select cardNo from t_avl_idcard_no where status=%s LIMIT 1;'
    result = mysql.getOne(sql_select,[0])  # 返回一个元组
    return result
    # for i in result:
    #     print(i)

def updateIDCard(cardNo):
    mysql = MysqlHelp('fastrunner')
    sql_update = 'update t_avl_idcard_no set status=%s, useage=%s where cardNo=%s;'
    mysql.sql_execute(sql_update, ['1', "api auto test", cardNo])

def getAndUpdateIDCard():
    # 创建一个实例对象，把数据库传进去
    mysql = MysqlHelp('fastrunner')
    sql_select = 'select cardNo from t_avl_idcard_no where status=%s LIMIT 1;'
    result = mysql.getOne(sql_select,[0])  # 返回一个元组
    sql_update = 'update t_avl_idcard_no set status=%s, useage=%s where cardNo=%s;'
    mysql.sql_execute(sql_update, ['1', "api auto test", result[0]])
    return result[0]

def getAndUpdatePhoneNo():
    # 创建一个实例对象，把数据库传进去
    mysql = MysqlHelp('fastrunner')
    sql_select = 'select phoneNo from t_avl_phone_no where status=%s LIMIT 1;'
    result = mysql.getOne(sql_select,[0])  # 返回一个元组
    sql_update = 'update t_avl_phone_no set status=%s, useage=%s where phoneNo=%s;'
    mysql.sql_execute(sql_update, ['1', "api auto test", result[0]])
    return result[0]

def getCurSeq():
    # 创建一个实例对象，把数据库传进去
    mysql = MysqlHelp('fastrunner')
    sql_select = 'select no from t_last_sequence where type=%s;'
    result = mysql.getOne(sql_select,["0"])  # 返回一个元组
    return result

def updateCurSeq(no):
    mysql = MysqlHelp('fastrunner')
    sql_update = 'update t_last_sequence set no=%s where type=%s;'
    mysql.sql_execute(sql_update, [no, "0"])

def getAndUpdateSeq():
    # 创建一个实例对象，把数据库传进去
    mysql = MysqlHelp('fastrunner')
    sql_select = 'select no from t_last_sequence where type=%s;'
    result = mysql.getOne(sql_select,["0"])  # 返回一个元组
    sql_update = 'update t_last_sequence set no=%s where type=%s;'
    mysql.sql_execute(sql_update, [result[0]+1, "0"])
    return result[0]+1

def updateCurSeq(no):
    mysql = MysqlHelp('fastrunner')
    sql_update = 'update t_last_sequence set no=%s where type=%s;'
    mysql.sql_execute(sql_update, [no, "0"])

def genNo():
    result = getAndUpdateSeq()
    return result


def getInterface(url, method):
    mysql = MysqlHelp('fastrunner')
    sql_select = 'select * from api where url=%s and method=%s LIMIT 1;'
    result = mysql.getOne(sql_select, [url, method])  # 返回一个元组
    return result

def updateInterface(url, method, interface):
    import time
    mysql = MysqlHelp('fastrunner')
    json_str = str(interface)
    sql_update = 'update api set update_time=%s, name=%s, body=%s, relation=%s, project_id=%s where url=%s and method=%s;'
    mysql.sql_execute(sql_update, [time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),interface["name"],json_str,4,3,url,method])

def insertInterface():
    import time
    from paserSwagger import getInterfaces
    interfaces = getInterfaces()
    mysql = MysqlHelp('fastrunner')
    # i=0
    for interface in interfaces:
        url = interface["request"]["url"]
        method = interface["request"]["method"]
        json_str = str(interface)
        if getInterface(url,method):
            updateInterface(url,method,interface)
            print("update")
        else:
            print("insert")
            sql_insert = 'insert into api(create_time, update_time, name, body, url, method, relation, project_id) values(%s, %s, %s, %s, %s, %s, %s, %s);'
            mysql.sql_execute(sql_insert, [time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),interface["name"], json_str,url,method,4,3])


if __name__ == '__main__':
    # for i in range(1,100000):
    #     insertPhoneNo(i)
    # result = getInterface('/api/caas/equipment/getAllDevPlcInfo','GET')
    # if result:
    #     for record in result:
    #         print(record)
    #     # updateIDCard(record)
    # else:
    #     print("no data found!")
    # no = getAndUpdatePhoneNo()
    # print(no)
    insertInterface()
    # updateInterface('/api/caas/collectSource/infos','GET',{'name': '采集源查询接口', 'times': 1, 'request': {'url': '/api/caas/collectSource/infos', 'method': 'GET', 'params': {'page': '', 'row': '', 'data.collectSourceType': '', 'data.collectSourceName': '', 'data.collectSourceId': '', 'data.factoryId': '', 'data.status': ''}}, 'desc': {'header': {}, 'data': {}, 'files': {}, 'params': {'page': '', 'row': '', 'data.collectSourceType': '', 'data.collectSourceName': '', 'data.collectSourceId': '', 'data.factoryId': '', 'data.status': ''}, 'variables': {}, 'extract': {}}})
