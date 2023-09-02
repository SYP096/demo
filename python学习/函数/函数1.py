# 函数就是执行特定任务和完成特定功能的一段代码
'''
为什么需要函数?
1 复用代码
2 隐藏实现细节
3 提高可维护性
4 提高可读性便于调试'''

# 函数的创建： 用到 def
'''
def 函数名([形参])
    函数体
    return[]'''
# 1，位置实参 2，关键词实参


def fun(a, b):
    c = a+b
    return (c)


a = fun(10, 20)
print(type(a), a)
'''出现的错误
1 函数前后要有两行空行(two blank lines)
2 def 后面要有 :
3 return 要在def内部,且return后面得有空格'''
# 多个返回值的时候，返回的结果为元组


def fun1(num):         # 这个是有没有用到*， 也就是说列表num是以一个实参代入到了函数
    odd = []     # 奇数
    even = []    # 偶数
    print(type(num))     # 这个时候列表num已经成功进入到了函数中，而且是以列表的形式
    for i in num:        # 列表的遍历还是要用到for in
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return (odd, even)


num = [12, 32, 43, 54, 32, 76, 67, 98, 89]
print(fun1(num))   # 调用函数要用到函数名字，以及要把实参和形参搞明白
# 多个返回值的话会以元组的形式返回到调用的位置


def fun1(*a):
    return a


a = (13, 14, 15, 16)
print(fun1(a))