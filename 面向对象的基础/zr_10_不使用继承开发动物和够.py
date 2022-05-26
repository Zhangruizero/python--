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


wangcai = Animal("旺财")


wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()

tom = Dog("tom")
tom.run()
tom.bark()