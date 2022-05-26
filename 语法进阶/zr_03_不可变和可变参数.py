def demo(num, num_list):
    print("函数内部的代码")
    num = 100
    num_list = [1, 2, 3]
    print(num)
    print(num_list)
    print("函数完成输出")


gl_num = 99
gl_list = [2, 3, 4]
demo(gl_num, gl_list)
print(gl_num, gl_list)