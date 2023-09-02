s = "huawei is a best"
print(type(s), s)
print(s.count('s'))
ss = s.count('s')
print(ss)
print(s.capitalize())
print(s.endswith('t'))
nam = s.endswith('t')
print(nam)
man = s.startswith('h')
print(man)
print(s.isdigit())
num = '12353453'
print(num.isdigit())
print(num.isdecimal())
nri = '四十'
print(nri.isdigit())
num1 =num.isdecimal()
print(num1)
aa = 'ace123'
aaa = aa.isalnum()
print(aa,aaa)
print(aa.isidentifier())
print(s.isidentifier(), '\n'.isspace())
sa = 'adc四'
print(sa.isalnum())
kk = "hello,hello,hello,world"
k = kk.replace('hello', 'qunide')      # 替换
print(kk.replace('hello', 'qunide', 1))
print(k, kk)
dfg = ['caca', 'cacca', 'acaacc']
print('|'.join(dfg))       # 合并
print('&'.join(dfg))
print('\t'.join(dfg))
print(chr(26472))         # 根据ordinal value 获取对应的字符
print(kk is k)      # 比较内存地址id
print(kk is not k)
print(ord('1'))        # 获取对应字符的ordinal value