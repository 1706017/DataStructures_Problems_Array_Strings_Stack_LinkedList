numbers1 = [12,13,15,18,-12,13,-18]
numbers2 = [12,13,14,15]
numbers3 = [1,-1,2,-2]


def check_sum_zero_or_not(num:list):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j] == 0:
                return True
    return False

print(check_sum_zero_or_not(numbers1))
print(check_sum_zero_or_not(numbers2))
print(check_sum_zero_or_not(numbers3))


#OUTPUT
#True
#False
#True
