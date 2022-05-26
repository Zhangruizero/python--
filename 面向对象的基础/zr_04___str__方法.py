class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")

        self.name = new_name

    def __del__(self):
        print("%s删除完成" % self.name)

    def __str__(self):
        # 此方法必须返回一个字符串
        return "woshimao"


tom = Cat("tom")
print(tom)
