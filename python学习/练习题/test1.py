a = int('123', 16)
print(a)
print(abs(-99))       # 绝对值
n = int(input("整数"))
print(n & 1 == n % 2)
print(round(3.4))
print(1, 2, 3, sep=',')
print('abc10'.isalnum())
print(len('中国'.encode('gbk')))     # 一个汉字在gbk是两个字符
print(len('中国'.encode('UTF-8')))   # 一个汉字在UFT-8是三个字符

dic = {1: 2, 2: 3, 3: 4}
aa = dic.pop(1)
print(type(aa))
print(aa)
dic.update({2: 4})
print(dic)
tupp = {1, 2, 3, 4, 5}
tupp.update([1, 2])
print(tupp)

for i in range(6):
    print(i)
    
a = 2.07
print('benim ganom', a)