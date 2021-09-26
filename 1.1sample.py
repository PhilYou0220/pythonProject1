"""工作打卡截图"""
from compare import compare
from whole_sanptime import whole_snap_time
import time
data = {'carNum': '', 'createdAt': 1611660907, 'endWeight': 0, 'id': 38}
# print(ss1["data"])
ss = {'data': [{'carNum': '', 'createdAt': 1611660907, 'endWeight': 0, 'id': 37}]}
a = str(time.time())
b = a.split(".")[0]
compare(data, ss)

whole_snap_time(b)

# data1 = data
#
# my_data = []
#
# for m in data.items():
#     # 取出了所有的key,形式是字符串,存到my_data中 ['carNum', 'createdAt', 'endWeight', 'id']
#     my_data.append(m[0])
#
# # [{'carNum': '', 'createdAt': 1611660907, 'endWeight': 0, 'id': 38}] 这种了
# ss1 = ss["data"]
# # my_ss现在是个字典了，{'carNum': '', 'createdAt': 1611660907, 'endWeight': 0, 'id': 38}这种了
# my_ss = ss1[0]
# for n in range(0, len(my_data)):
#     # 防止传参时值为空
#     if data1[my_data[n]] != "":
#         # 判断值是否相等
#         if data1[my_data[n]] == my_ss[my_data[n]]:
#             print("传、返参数{}和传、返回值的{}是一致的".format(my_data[n], my_ss[my_data[n]]))
#         else:
#             print("传、返参数为{},传、返回值为{}和{}不一致！！！".format(my_data[n], data1[my_data[n]], my_ss[my_data[n]]))
#     else:
#         print("传入参数{}是空的".format(my_data[n]))
