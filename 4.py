# a = 1
# print("你的%s"%a)
import os
a = 'Break' if os.name == 'nt' else '非windows系统'
print(a))