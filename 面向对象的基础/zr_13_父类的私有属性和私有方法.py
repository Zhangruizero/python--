class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def _test(self):
        print("私有方法%d %d" % (self.num1, self.__num2))


class B(A):
    def demo(self):
        # 1.在子类的对象方法中不能访问父类的私有属性
        pass
        # 2.在子类的对象方法中不能调用父类的私有方法


b = B()
print(b)