num_a = int(input('请输入第一个整数'))
num_b = int(input('请输入第二个整数'))
'''
if num_a >= num_b:
    print(str(num_a) + '大于等于' + str(num_b))
else:
    print(str(num_a) + '小于' + str(num_b))
         !!!字符串是无法正确比较大小的
'''
# 使用条件表达式进行比较，只用一行代码就可以了
print(str(num_a) + '大于等于' + str(num_b) if num_a >= num_b else str(num_a) + '小于' + str(num_b))
# 如果条件表达式结果为true， 执行if前面的代码，否则（也就是结果为False），执行else之后的代码