class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))

    def __secret(self):
            print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("曹芳")


# 私有属性和私有方法不能再外界直接访问
# xiaofang.__secret()
xiaofang.secret()

# 伪私有属性和方法

print(xiaofang._Women__age)

xiaofang._Women__secret()