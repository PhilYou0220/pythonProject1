# a = {"i":"sss", "o":123}
# b = {"id":1,"name":"zhangsan"}
# c = {"age":18,"gender":"male"}
# b = a.get("i")
# c = a.values()
# d= list(a.keys())
# f = list(a.items())
# print(a)
# print(b)
# print(c)
# print(d)
# print(f)



# res = a.keys()  ^ c.keys()


#
# print(res)

a= {"i":1,"b":2}
b = {"i":2}
print(a.keys())
print(b.keys())
result = a.keys() or b.keys()
print(result)

# c = {"apple", "banana", "cherry"}
# d = {"apple1", "banana", "cherry"}
# e = {"aa"}
# print(c and d)
