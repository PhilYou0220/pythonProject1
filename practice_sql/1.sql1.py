import pymysql

try:
    # 连接数据库格式
    conn = pymysql.connect(host='localhost', user='root', password='YOUfei1!', database='youfei')
except:
    print("连接失败")
else:
    # 默认将为元组，cursor=pymysql.cursors.DictCursor针对的后面的cursor与前面的变量无关，将其转为字典类型，因为是cursor执行的
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from user limit 10"
    print(sql)
    cursor.execute(sql)
    # fetchone 取一行，fetchall取全部的fetch取多行
    result = cursor.fetchall()
    print(result)
    # 先关游标
    cursor.close()
    # 关闭连接
    conn.close()