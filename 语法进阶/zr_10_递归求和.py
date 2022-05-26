def sum_numbers(num):
    # 1.递归出口
    if num == 1:
        return 1
    num += sum_numbers(num - 1)
    return num


result = sum_numbers(100)
print(result)
