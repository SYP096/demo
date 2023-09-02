import recursive
num = recursive.fac(9)
print(num)
# 模块必须得置顶
# print('------------另一个写法-----------')
'''from recursive import fac'''
# num = fac(9)     # 用到from时，就不需要句点.了
# print(num)
'''print('--------用到as起外号----------')'''
# from fibnocci import fib as f
# num = f(9)
# print(num)
# import recursive as dg
# num = dg.fac(8)
# print(num)