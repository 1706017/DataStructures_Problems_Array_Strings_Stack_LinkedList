data = [12,14,56,89,90.13]

def func_find_second_largest(numbers:list):
    first_max = max(numbers[0],numbers[1])
    sec_max = min(numbers[0],numbers[1])
    for i in range(2,len(numbers)):
        if numbers[i] > first_max:
            sec_max = first_max
            first_max = numbers[i]
        elif numbers[i] > sec_max and first_max!= numbers[i] :
            sec_max = numbers[i]
    return sec_max

print("The second largest element in list is : ",func_find_second_largest(data))
