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



print(numberOfSteps(8))
