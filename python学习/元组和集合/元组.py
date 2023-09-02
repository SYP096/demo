# 元组是一个python内置的数据结构，是有序的 不可变序列。
t = ('python', 'hello', 90)
# t = 'python', 'hello', 90   也可以不带小括号
name = tuple(('python', 'first', 99))    # 这里必须带括号，双括号
print(type(t), '\t', t)
print(type(name), '\t', name)
__name__ = ('python',)
print(type(__name__), '\t', __name__)
s = ('python', 'hello', [10, 20, 30, 40, 'China', 'Turk'], 90, 80)
print(type(s), '\t', s) 
print('-------------以下是新增操作-----------')          # 元组中是可以有列表的，而且这个列表内的元素是可以改动的
s[2].append(99)     # 元组中的列表是可以改动的 append
print(s)
s[2].insert(4, 50)   # 也可以用insert进行插入 操作
print(s)
sss = [60, 70, 80, 90]
s[2].extend(sss)    # 也可以用extend进行新增操作
print(s)
print()
print('------------以下是删除操作-----------')
ss = s[2].pop(-1)    # 可以用pop 弹出某个指定的数据， 并且可以使用
print(s)
print(type(ss), '\t', ss)
s[2].remove('China')    # 使用remove删除
print(s)
s[2].clear()    # 也可以使该列表变成空值
print(s)
for i in s:       # 遍历元组 使用 for-inS
    print(type(i), '\t', i)
'''
元组中的列表只能新增, 删除, 不能修改，
也不能使用 切片 和 del函数
'''
# 元组 没有 元组生成式