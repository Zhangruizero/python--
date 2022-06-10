class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):

        return "%s 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具列表名称
        self.item_list = []

    def __str__(self):

        return("户型： %s\n总面积： %.2f[剩余： %.2f]\n家具：%s"
               % (self.house_type, self.area,
                  self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)
        # 判断家具面积
        if item.area > self.free_area:
            print("%家具过大,无法添加" % item.name)
            return
        # 将家具名称添加入家具列表中
        self.item_list.append(item.name)
        # 计算剩余面积
        self.free_area -= item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

# 创建房子的对象
my_house = House("两室一厅", 60)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print(my_house)