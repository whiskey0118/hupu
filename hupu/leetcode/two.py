#给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1
def two(num):
    s=0
    while(num>0):
        if num%2 ==0:
            num = num/2
        else:
            num = num-1
        s=s+1
        # print(s)
    return s

def numberOfSteps(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if num % 2 == 0:
        print(num)
        return numberOfSteps(num / 2) + 1
    else:
        # print(num)
        return numberOfSteps(num - 1) + 1

print(two(14))