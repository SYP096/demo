'''打印一个三行四列的矩阵'''
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')    # 后面带一个制表位
    print()
else:
    print('以下是九九乘法表')

'''带你一个九九乘法表'''
for i in range(1, 10):       # 这个是自动换行的
    for j in range(1, i+1):
        print(i, '*', j, '=', i*j, end='\t')     # 如果输出有整数和字符串，那么用 , 就行
    print()    # 换行                            # 想用 + 的话，得用上str(i) 和 str(j)
# 如果没有这个 print() 就不会自定换行了
# 因为循环里面有输出才会自动换行，就算这个输出为空值

'''多重循环中break和continue的使用'''

for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            #break
            continue
        print(j, end='\t')
    print()
# break 和 continue 指挥控制本层循环，不影响外层循环