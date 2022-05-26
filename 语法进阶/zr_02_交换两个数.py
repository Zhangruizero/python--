a = 6
b = 100

# # 解法一
# c = a
# a = b
# b = c


# # 法2
# a = a + b
# b = a - b
# a = a - b

# py 专有
a, b = (b, a)
# a, b = b, a

print(a)
print(b)
