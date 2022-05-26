class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
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
        print("%s汪汪" % self.name )

class Xiaotianquan(Dog):
    def __init__(self, new_name):
        self.name = new_name

    def fly(self):
        print("%s会飞" % self.name)

    def bark(self):
        print("%s呜呜" % self.name )

# 果如子类中，重写父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法

xtq = Xiaotianquan("天狗")
xtq.bark()