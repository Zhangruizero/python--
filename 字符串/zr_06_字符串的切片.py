num_str = "0123456789"

# 1.截取从2-5位置的字符串
a = num_str[2:6]
print(a)
# 2.截取从2-末尾的字符串
b = num_str[2:]
print(b)
# 3.截取从开始-5位置的字符串
c = num_str[:6]
print(c)
# 4.截取完整的字符串
d = num_str[:]
print(d)
# 5.从开始位置，每隔一个字符截取字符串
e = num_str[::2]
print(e)
# 6.从索引1开始，每隔一个取一个
f = num_str[1::2]
print(f)
# 7.截取从2-末尾-1的字符串
g = num_str[2:-1]
print(g)
# 8.截取字符串末尾两个字符
h = num_str[-2:]
print(h)
# 9.字符串的逆序
i = num_str[-1::-1]
j = num_str[::-1]
print(i)
print(j)