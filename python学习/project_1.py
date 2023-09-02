s = input().lower()
alpha, space, digit, others = 0, 0, 0, 0
for i in s:
    if 'a' <= i <= 'z':        # alpha就是英文字母
        alpha += 1
    elif i == ' ':             # space就是空格
        space += 1
    elif '0' <= i <= '9':      # digit就是数字
        digit += 1
    else:
        others += 1
print("英文字母: ", alpha)
print("空格: ", space)
print("数字: ", digit)
print("其它字符: ", others)