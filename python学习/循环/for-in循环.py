for _ in range(10):
    print(_)
for _ in range(10):
    print('薛之谦')
print('————使用for循环计算1到100的偶数和————')
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print('1到100之间的偶数和为{}'.format(sum))

# 用for-in计算出100到999之间的水仙花数
for i in range(100, 1000):
    if i == (i // 100 % 10)**3 + (i // 10 % 10)**3 + (i % 10)**3:
        print('100到999之间的水仙花数有{}'.format(i))