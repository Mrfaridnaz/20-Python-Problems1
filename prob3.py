# 3 Find the maximum Element in a list
def find_max(numbers):

    if not numbers:
        return None

    max_value = numbers[0] # 1, 12, 23, 74

    for num in numbers[1:]: # 12,23,74,43, 2
        if num > max_value: # num = 12>1, 23>12, 74>23, 43>74, 2>74
            max_value = num
    return max_value

li = [1,12,23,74,43,2, 434, 342342342, 2424,234242]
print(find_max(li))