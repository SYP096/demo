def fac(n):
    # 递归函数， 6！= 6*5*4*3*2*1
    if n == 1:
        return (1)
    else:
        num = n*fac(n-1)
        print(n)    # 打印n，num 只是为了更好的理解这个函数，导入的时候记得把这两行注释
        print(num)   # 用小虫子可以看到，会在这里一个个销毁之前的函数
        return (num)      # 也就是说fac(n-1),已经做完了，所有的职业已经存贮了，就剩使用这些数值去计算num值了
    

print(fac(6))

# 语法结构就是 if elif  else