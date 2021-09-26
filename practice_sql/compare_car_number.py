"""对比数据 对比一个大的集合的数据不在他的子集数据中的额外数据
如运企提供的车牌是否都在数据库中 第一列放运企的车牌 第二列放数据库的车牌 车牌都是唯一的才行 不需要表头"""
import xlrd
import xlwt
import time
my_excel = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\不在数据库的二标段.xls")
my_sheet = my_excel.sheet_by_index(0)
all_row = my_sheet.nrows
all_col = my_sheet.ncols
print(all_col)


# xlrd 用的with open因此不用关闭
for i in range(0, all_col):
    if i == 0:
        # 读取第一列的所有数据，还有start_rowx end_rowx content1会作为一个列表存储数据
        content1 = my_sheet.col_values(colx=i)
    elif i == 1:
        content2 = my_sheet.col_values(colx=i)

different_data = []

print(content1)
print(content2)
for j in content2:
    if j not in content1:
        different_data.append(j)

print("*"*11*len(different_data))
out_all_rows =len(different_data)
print("数据个数为{}".format(out_all_rows))
print(different_data)

# 新建一个excel
out_excel = xlwt.Workbook(encoding="utf-8")
# 新建一个sheet
out_sheet1 = out_excel.add_sheet("sheet1")
# write(x,y,z)三个参数:x 行号 y 列号 z数据行列从0开始计数
for k in range(0, out_all_rows):
    out_sheet1.write(k, 0, different_data[k])

out_excel.save(r"C:\Users\Administrator\Desktop\{}.xls".format(time.strftime("%Y_%m_%d %H_%M_%S")))











