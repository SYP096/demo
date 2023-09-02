'''从键盘输入密码，最多输入三次，如果正确就结束循环'''
'''
for item in range(3):
    password = input('请输入密码')
    if password == '8888':
        print('密码正确')
        break              # 如果输入密码为8888，则密码正确，跳出循环
    else:
        print('密码不正确，请重新输入')


num = 0
while num < 3:
    psw = input('请输入密码')
    if psw == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    num += 1         # num += 1 可以放在while的循环内，也可以放在if else内

# break 对于 for-in 和 while 的作用是一样的

# 使用 continue 找到1-50之间5的倍数

for item in range(1, 51):
    if item % 5 == 0:     # 也可以是 if not bool(item%5):      if not item%5:
        print(item)
print('-------使用continue-------')

for i in range(1, 51):
    if i%5 != 0:      # 也可以是 if item%5:
        continue
    else:
        print(item)
'''
for item in range(3):
    password = input('请输入密码')
    if password == '8888':
        print('密码正确')
        break              # 如果输入密码为8888，则密码正确，跳出循环
    else:
        print('密码不正确，请重新输入')
else:                       # 这个else是循环结束之后才会执行的，遇到break则不执行
    print('抱歉，您输入的三次密码都是错误的')