def fun(a, b):
    global c  # 如果想要把c定义成全局变量，得再def下面第一行定义，加上global
    c = a+b
    return c


num = fun(11, 22)
print(c)   # c 为局部变量，不能在函数外使用，除非使用global
print(num)