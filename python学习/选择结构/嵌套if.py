'''
会员   >=200  打8折
       >=100  打9折
       <100   不打折
非会员  >= 200  打9.5折
        < 200   不打折
'''
answer = input('请问您是会员吗？ y/n')
money = float(input('请输入您的购物金额：'))
if answer == 'y':   # 会员
    if money >= 200:
        print('打八折，您需要支付的金额为：', money*0.8)
    elif money >= 100:
        print('打九折，你需要支付的金额为', money*0.9)
    else:
        print('不打折，您需要支付的金额为', money)
else:      # 非会员
    if money >= 200:
        print('打九五折，您需要支付的金额为：', money*0.95)
    else:
        print('不打折，您需要支付的金额为:', money)