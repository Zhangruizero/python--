j = 1
while j <= 9:
    a = 1
    while a <= j:
        print("%d * %d = %d" % (a, j, a * j), end="\t")  # \t在控制台输出一个制表符， 协助在输出文本时垂直方向的对齐
        a += 1
    print("")  # 添加换行
    j += 1
