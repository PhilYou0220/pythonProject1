import pymysql

conn = pymysql.connect(host='localhost', user='root', password='YOUfei1!', database='youfei')

cursor = conn.cursor()
# 插入insert sql
my_sql = "insert into user(username,password)values('faker','1')"
print(my_sql)
if cursor.execute(my_sql):
    print("插入成功")
else:
    print("失败！")
# cursor.lastrowid是查询最新的主键id，要写在commit之前才行，否则会返回None
print(cursor.lastrowid)

# 进行增，删，改需要提交，查询不需要进行提交
conn.commit()
my_sql2 = "select * from user"
cursor.execute(my_sql2)
result = cursor.fetchall()
print(result)

# 删除delete sql 里面单引号才行如'faker‘
my_sql3 = "delete from user where username = 'faker'"
cursor.execute(my_sql3)
conn.commit()
cursor.execute(my_sql2)
result = cursor.fetchall()
print(result)
# 更新 update
my_sql4 = "update user set username='uzi3' where username='uzi2' "
cursor.execute(my_sql4)
conn.commit()
cursor.execute(my_sql2)
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()
