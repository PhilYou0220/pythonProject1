import copy

start_list = "[1, 2, 3]"
# end_list = start_list
# end_list = []
end_list = copy.deepcopy(start_list)
# 会输出直接赋值使用相同的内
# 存地址
if id(start_list) == id(end_list):
    print("直接赋值使用相同的内存地址")
else:
    print("直接赋值内存地址不一致")

end_list = start_list

# del start_list[0]
# 会输出切片赋值内存地址不一致
if id(start_list) == id(end_list):
    print("切片赋值使用相同的内存地址")
else:
    print("切片赋值内存地址不一致")
print('start_list 列表：', start_list)  # start_list 列表： []
print('end_list 列表：', end_list)  # end_list 列表： [3]
