# 这个是银行取款机的代码，根据kurs 中func倒数第二单元写的
mustafa = {
                'name': 'Mustafa',
                'hesapno': 9349583,
                'bakiye': 3000,
                'ekhesap': 2000       # ekhesap 就是可以透支的金额
            }

ali = {
        'name': 'Ali',
        'hesapno': 35473674,
        'bakiye': 2000,
        'ekhesap': 1000
    }


def bankamatik(account, money):
    balance(account=account)
    if account['bakiye'] >= money:
        print(f"Hello, {account['name']}, you can take the money \n")
        account['bakiye'] -= money
        balance(account=account)        # 在函数内部召唤另一个函数
    elif account['bakiye'] < money:
        judge = input(f"Hello, {account['name']}, you don't have enough balance, do you plan to use ekaccount? (y/n) \n")
        if judge.lower() == 'y':
            total = account['bakiye'] + account['ekhesap']
            if total >= money:
                print(f"Heelo, {account['name']}, you can take the money \n")
                account['bakiye'] = 0
                account['ekhesap'] = total - money
                balance(account=account)
            elif total < money:
                print(f"Hello, {account['name']}, you don't have enough balance \n")
                balance(account=account)
        elif judge.lower() == 'n':
            print(f"Hello, {account['name']}, welcome to come again nxet time")


def balance(account):
    print(f"{account['name']}, your balance is {account['bakiye']}, and your ekaccount is {account['ekhesap']} \n")


bankamatik(mustafa, 2000)
bankamatik(ali, 3000)
