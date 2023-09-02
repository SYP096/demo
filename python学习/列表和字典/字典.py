scores = {'张三': 100, '李四': 98, '王五': 66}
wan = scores['张三']
print(scores)
print(wan)
sun = scores.get('按错技能', 55)
print(sun)
scores['yapeng'] = 99     # 新增key-value对
print(scores)
scores['yapeng'] = 89     # 修改value
print(scores)
print()

values = scores.values()
print(values)       # 输出为 dict_values 格式
print(type(values))
print(list(values))     # 用内置函数 list() 转化为字典
print()

keys = scores.keys()
print(keys)         # 输出为 dict_keys 格式
print(type(keys))
print(list(keys))    # 用内置函数 list() 转化为字典
print()

items = scores.items()      # 可以用于从字典中提取元组
print(items)                # 输出为 dict_items 格式
print(type(items))
print(list(items))       # 用内置函数 list() 转化为字典，且 此字典由元组组成，元组的内容是key-value.
print()
del scores['张三']      # 字典中删除某一个指定元素只能用del  , clear() 是清除所有元素
print(scores)

# 字典生成式
