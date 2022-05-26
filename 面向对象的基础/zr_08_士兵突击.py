class Gun:
    def __init__(self, model):
        self.module = model
        self.bullet_count = 0

    def add_buttlet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("无弹药")
            return
        self.bullet_count -= 1
        print("%s 发射。。。【%d】" % (self.module, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("%s 还没枪" % self.name)
            return

        print("冲   %s" % self.name)

        self.gun.add_buttlet(50)

        self.gun.shoot()


ak47 = Gun("AK47")

xusanduo = Soldier("许三多")


xusanduo.gun = ak47

xusanduo.fire()
print(xusanduo.gun)
