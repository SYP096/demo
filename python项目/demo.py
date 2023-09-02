from bankamatik import bankamatik
'''
这个demo是试着导入本文件夹的bankamatik函数
导入时别忘了归置bankamatik函数文件中的打印输出
但是导入这个模块时， 会自动出现一个__pycache__文件
'''
muhammed = {
                    'name': 'muhammed',
                    'hesapno': 836275617,
                    'bakiye': 9000,
                    'ekhesap': 5000
                }
bankamatik(muhammed, 10000)
# 如果只是import bankamatik, 必须是 bankamatik.bankamatik(account, money)
