def fib(n):
    # 用递归实现斐波那契数列
    if n == 1:
        return (1)
    elif n == 2:
        return (1)
    else:
        num = fib(n-1) + fib(n-2)    # 先调用n-1， n-1执行结束后，调用n-2
        print(n)
        print(num)
        return (num)


print(fib(6))      # 斐波那契 0 1 1 2 3 5 8 13 21
# print('------------查看斐波那契前六个数字----------')
# for i in range(1, 7):
#     print(fib(i))