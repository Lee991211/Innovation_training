import time
import pymysql
import csv

def get_time():
    time_str =  time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="47.98.141.4",
                           # port=3306,
                           user="test",
                           password="123456",
                           db="innotrain",
                           charset="utf8mb4")
    # 创建游标
    cursor = conn.cursor()# 执行完毕返回的结果集默认以元组显示
    return conn, cursor

def close_conn(conn, cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql)
    # cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_predict(plat):
    sql = "select ds,emotion_val,topic, platform from emotion_val where predict=1 and platform =%s order by ds"%plat
    res = query(sql)
    return res

def get_emotion_val(plat):
    sql = "select ds,emotion_val,topic,predict from emotion_val where platform =%s order by predict"%plat
    res = query(sql)
    return res

def get_rawdata(plat):
    sql = "select context,ds,topic from raw_data where platform =%s "%plat
    res = query(sql)
    return res

def get_midrawdata(plat):
    sql = "select ds,emotion_val,topic from emotion_val where predict=0 and platform =%s order by ds"%plat
    res = query(sql)
    return res


# def get_l1_data():
#
# 	sql = "select ds,confirm,suspect,heal,dead from history"
# 	res = query(sql)
# 	return res
#
# def get_l2_data():
#
# 	sql = "select ds,confirm_add,suspect_add from history"
# 	res = query(sql)
# 	return res
#将CSV文件处理为dict在转换为json格式数据
# def dataprocess(file):



if __name__ == "__main__":
    print()