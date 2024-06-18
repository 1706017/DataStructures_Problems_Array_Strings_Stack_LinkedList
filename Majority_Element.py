def fun_find_majority_element(numbers:list):
    compare_with = len(numbers)/2
    for i in range(len(numbers)):
        count = 1
        for j in range(i+1,len(numbers)):
            if numbers[i] == numbers[j]:
                count = count + 1
            else:
                continue
        if count > compare_with:
            return numbers[i]
    return None



num1 = [2,2,3,3,56,3,3,7,8,3,3]

print(fun_find_majority_element(num1))
