def fun(a, b):
    print(a, b)


fun(10, 20)


def fun(a, b=100):   # b=100 中间不能有空格，这个属于默认值
    c = a + b
    return (c)


c = fun(200, 200)   # 默认值是可以被替代的，如果没有第二个200，b将默认为100
print(c)


def fun1(*num):
    print(num)    # 输出为元组  


fun1(88)      # 只要带上了*，输出皆为元组
fun1(99, 10, 22)


def fun2(**num):
    print(num)      # ** 必须和关键字实参一起使用，输出为列表


fun2(a=11, b=22, c=33, d=44)


def fun3(a, b, c):
    print('a=', a)
    print('b=', b)
    print('a=', c)


lis = [11, 22, 33]
fun3(*lis)     # 如果想让列表中的元素进入到函数fun1， 需要加上*,类似于位置实参
print('---------------------------------')
dic = {'c': 11, 'b': 22, 'a': 33}
fun3(**dic)    # 字典必须加上**， 类似于关键字实参


def fun4(a, b, *, c, d):
    print('a=', a)
    print('b=', b)
    print('a=', c)
    print('d=', d)


print('--------------------')
fun4(11, 22, c=33, d=44)
fun4(a=11, b=22, c=33, d=44)

print('---------形参的顺序问题---------')


def fun5(a, b, *, c, d, **f):      # 
    pass


def fun6(*ee, **ff):
    pass


def fun7(a, b=10, *, c, **fff):
    pass