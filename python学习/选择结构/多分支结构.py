'''多分支结构
成绩范围  0-100
A  90-100
B  80-89
C  79-79
D  60-69
E  0-59
如果数值不在0-100的范围内的话, 该数值为非法数值
'''

num = int(input('请输入一个成绩:'))
if 90 <= num <= 100:            # 或者 num >= 90 and num <= 100
    print('该学生的成绩为A')
elif 80 <= num <= 89:           # 或者 num >= 80 and num <= 89
    print('该学生成绩为B')
elif 70 <= num <= 79:           # 以下都可以使用and
    print('该学生成绩为C')
elif 60 <= num <= 69:
    print('该学生成绩为D')
elif 0 <= num <= 59:
    print('该学生成绩为E')
else:
    print('对不起, 成绩有误, 不在成绩有效范围')