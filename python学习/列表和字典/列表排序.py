list = [22, 12, 24, 65, 77, 98, 222, -2, -99, -21, 645, 55, 44]
new_list = sorted(list)
print(list, '\n', id(list))
print(new_list, '\n', id(new_list))
newest_list = sorted(list, reverse=True)
print(newest_list, '\n', id(newest_list))
newest_list.sort()
print(newest_list, '\n', id(newest_list))
list1 = ['happ', 'Eadac', 'eadac', 'ijacoaijo', 'aasd']
list1.sort(reverse=False)
print(list1)
print()
# 列表生成式
lis = [i*(i+2) for i in range(1, 10)]
print(lis)