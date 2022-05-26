class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        assert isinstance(self.name)
        print("%s吃" % self.name)

    def drink(self):
        print("%s喝" % self.name)

    def run(self):
        print("%s跑" % self.name)

    def sleep(self):
        print("%s睡" % self.name)


class Dog(Animal):
    def __init__(self, nwe_name):
        self.name = nwe_name

    def bark(self):
        print("%s汪汪" % self.name)


class Xiaotianquan(Dog):
    def __init__(self, new_name):
        self.name = new_name

    def fly(self):
        print("%s会飞" % self.name)

    def bark(self):
        # 1.正对子类的特有需求，编写代码
        print("%s 神一样的叫唤" % self.name)
        # 2.使用super（），调用原本在父类中封装的方法
        super().bark()
        print("%s*&(*&(" % self.name)


xtq = Xiaotianquan("天狗")
xtq.bark()