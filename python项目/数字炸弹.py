import random
# 数字炸弹就是随机抽取一个数字， 玩家猜到这个数字为止
num = random.randint(1, 100)          # 随机抽取一个整数
print(num)
a = 1
b = 100
while True:
    player_num = int(input("请输入一个数字："))
    if player_num == num:
        print("很遗憾，炸弹爆炸了")
        break
    else:
        if player_num > b or player_num < a:
            print("请输入范围内的数字")
            continue
        else:

            if a <= num <= player_num:
                b = player_num
                print(f'{a} - {b}')
            elif player_num <= num <= b:
                a = player_num
                print(f'{a} - {b}')
