def sy_hello():
    print("你好你好， 我是郭富城")


# 如果直接执行模块， __main__
if __name__ == "__main__":
    print(__name__)

    # 文件被导入时，能够直接执行的代码不需要被执行
    print("小明开发的模块")
    sy_hello()