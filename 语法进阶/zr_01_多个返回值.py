def measure():
    print("sdfs")
    temp = 39
    wetness = 50
    print("sdasd")

    return temp, wetness


restlt = measure()
print(restlt)

# 需要单独的处理温度和湿度
print(restlt[0])
print(restlt[1])

# 如果函数的返回类型时元组，可以使用多个变量一次接受函数返回结果
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)