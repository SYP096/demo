# 字典生成式
# 要用到内置函数 zip()
items = ['Books', 'Pencils', 'A4apers', 'Others']
prices = [99, 88, 77, 66]
lis = zip(items, prices)      # 使items和prices打包成zip文件
print(type(lis), lis, '\n')   # 可以看到zip文件无法之间查看，需要用到内置函数list()
print(list(lis))
'''
输出可以看到, 使用内置函数zip()是将items列表和prices列表作为参数,
将这两个列表中的元素相互对应打包成了一个个元组,然后返回由这些元组组成的列表。
# 打包的对象必须是可迭代对象
'''
# 输出为 [('Books', 99), ('Pencils', 88), ('A4papers', 77), ('Others', 66)]

print()
d = {item.upper(): price for item, price in zip(items, prices)}
print(type(d), '\t', d)
# 容易出错的地方
'''
: 冒号后面必须要跟一个空格, in 后面的可迭代对象 必须用zip()函数, 哪怕让zip()给到一个变量赋值
再使用这个变量都不行, 必须是zip()'''

# 列表生成式
lis = [i*(i+2) for i in range(1, 10)]
print(lis)