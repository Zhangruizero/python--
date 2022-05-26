class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫%s体重是%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s爱跑步" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 爱干饭，干完饭也不减肥" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75)


xiaomei =  Person("小美", 50)
xiaoming.run()
xiaoming.eat()


xiaomei.eat()
xiaomei.run()
print(xiaoming)
print(xiaomei)