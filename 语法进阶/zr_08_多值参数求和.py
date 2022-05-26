def sum_numbers(*num):
    # def sum_numbers(num):
    sum = 0
    for n in num:
        sum += n
    return sum


result = sum_numbers((1, 2, 3, 4, 5))
print(result)
