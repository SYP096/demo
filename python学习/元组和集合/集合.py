# 内置函数集合set()
# python 语言提供的内置函数，同列表一样，是无序的可变类型的序列
# 集合 是没有value的字典，形同于 dict_keys
s = {'china', 'turk', 'Rus', 10, 20, 30, 40}
print(type(s), '\t', s)
print(set(range(1, 10)))
ss = set(range(1, 10))      # 列表，元组， 字典， 字符串，range都可以转化为集合，也可以直接用来赋值
print(type(ss), '\t', ss, '\n')
print(set([10, 20, 30, 40]))     # 列表直接转化为集合
print(set((10, 20, 30, 40)))     # 元组直接转化为集合
print(set({'China': 99, 'Turk': 90}))    # 字典，只获取keys
print(set({'China', 'Rus'}))      # 集合到集合
print(set('python'))           # 字符串到结合
print(set())            # 空集合 只能用set() 创建空集合
s = {'China', 'turk', 'Rus', 10, 20, 30, 40}
print('----------以下是判断--------')    # 使用 in, not in
print(30 in s)
print('China' not in s)
print('------------以下是新增操作-----------')
s.add(50)    # add 一次是能添加一个元素
print(s)      # print(s.add(50))   以及    s = s.add(50) print(s)的输出结果为None
s.update([40, 50, 60, 70, 80, 90])     # update 一次添加至少一个元素，单个元素会报错
print(s)            # 使用update时， 可以把列表，字典，元组中的元素新增到集合，若有重复元素，只输出一次
# update and add 只能使用这种形式，其他形式会输出为None
print('------------以下是删除操作------------')
s.remove('Rus')   # remove 删除某个指定元素
print(s)
# s.remove(111)    # 使用remove时，集合中若无该元素，会报错，但discard不会报错
s.discard(111)     # 集合中没有111， 但是不会报错
s.discard('China')  # discard 也是删除某个元素，但是不会报错
print(s)
print('-----------pop()和其他函数不一样-----------')
s.pop()                 # pop 随即删除一个元素， pop 的意思是抛出
ss = s.pop()            # pop 随机删除一个元素，并且可以赋值，加以使用。 但也只有pop()
print(s)                
print(ss)
print(s.pop(), s)    # pop 也可以这样使用， 但也只有pop() 可以这样用
print(s, s.pop())    # 这两个格式都一样，前后顺序不影响什么
s.clear()             # 清空集合，空集合
print(s)

# 以上只用 pop() 可以用来赋值，其他的都不可以，会输出None
print('------------集合的遍历----------')
names = {'china', 'turk', 'Rus', 10, 20, 30, 40}
for name in names:         # 集合的遍历也是用 for-in
    print(type(name), '\t', name)
print('----------以下是集合的关系----------')
sun = {30, 20, 10}
mun = {10, 20, 30}
print(sun == mun)      # 是否相等用 ==  !=
print(sun != mun)
sun = {10, 20, 40, 30, 50}
print(mun.issubset(sun))      # mun 是 sun 的子集
'''asd = mun.issubset(sun)      可以用来赋值
print(asd) '''
print(sun.issuperset(mun))    # sun 是 mun 的超集
'''dsa = sun.issuperset(mun)       也可以用来赋值
print(dsa)'''
print(sun.isdisjoint(mun))      # 两个集合是否 没有交集....hjk = sun.isdisjoint(mun)也可以赋值
a = {10, 30, 60, 40}
b = {10, 20, 30, 50}
print(a.intersection(b))    # a and b 交集, 也可以是 a & b , a 与 b
print(a & b)
buv = a.intersection(b)     # 形成一个新的集合， id也不一样
print(buv, id(buv), '\n', id(a), id(b))
print(a.union(b))       # a and b 合集, 也可以是 a | b , a 或 b
print(a | b)
print(a.difference(b))    # 差集  去除a中 b集合的相同元素， 或者说，去除a中 a和b的交集  a - b
print(a - b)
print(b.difference(a))    # 差集  去除b中 a集合的相同元素, 同上， b - a
print(b - a)
print(a.symmetric_difference(b))      # 对称差集  a ^ b
print(a ^ b)
ilk = a ^ b
print(ilk)
# 以上集合间的关系都可以用来赋值成一个新的集合，并且加以运用
print('------------以下是集合生成式------------')
best = {i*(i+3) for i in range(1, 10)}  # for 之前的表达式可以写很多不一样的
print(type(best), id(best), best)
for i in best:
    print(i)     # 集合可以拿来遍历，但是不会按照顺序，因为集合是无序的