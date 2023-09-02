# 水仙花数指的是一个三位数的每个数字的三次方的和位这个三位数，比如153= 1+125+27
# 用循环便可以解决
for i in range(100, 1000):
    if (i // 100 % 10)**3 + (i // 10 % 10)**3 + (i % 10)**3 == i:
        print(i)
# 出错的地方
# 逗号后面一定要跟个空格， if 和 elif， else 后面也要跟个英文“:”，连续多个数字运算最好一起算。此时也得用==，因为有比较的含义在。
# + - * / 是最基本的加减乘除
# // 取整数的除法
# % 取余数的除法
# ** 次方

# 另一个表达式， if ()**3 + ()**3 + ()**3 != i:
#                   continue
#               else:
#                   print(i)