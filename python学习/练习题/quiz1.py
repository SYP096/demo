'''
给定一个整数数组 nums 和一个整数 target, 返回两个数字的索引, 使它们加起来等于 target。
您可能会假设每个输入只有一个解决方案, 并且您可能不会两次使用相同的元素。
您可以按任何顺序返回答案。
'''
nums = []
confirm = True     # confirm意思是确认，在这里判断是否继续循环
print("提醒您一下，如果您不打算输入整数了, 请输入0")   # judge 的意思是判断
while confirm:
    num = int(input("请输入一个整数："))
    nums.append(num)   
    if num == 0:
        nums.remove(0)
        break
if len(nums) >= 2:
    target = int(input("请再输入一个整数作为目标值："))
    a = 0
    b = 1
    while b < len(nums):
        if nums[a] + nums[b] == target:
            print(a, b)
            b += 1
            continue
        elif nums[b] != nums[-1]:
            b += 1
        elif nums[b] == nums[-1] and nums[a] == nums[-2]:
            break
        else:
            a += 1
            b = a+1
else:
    print("不好意思, 您少输入了{}个整数".format(2-len(nums)))
