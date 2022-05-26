students = [{"name": "阿土"},
            {"name": "小美"}]

find_name = "阿土"

for std in students:
    print(std)
    if std["name"] == find_name:
        print("找到了")
        break
else:
    print("抱歉没找到 %s" % find_name)
