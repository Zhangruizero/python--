import order_tool
import datetime

while True:

    order_tool.show_menu()
    action = input("请选择执行的操作：")
    print("您选择的操作是：%s" % action)

    if action in ["1", "2", "3", "4", "5"]:
        if action == "1":
            order_tool.booking()
        if action == "2":
            order_tool.tuipiao()
        if action == "3":
            order_tool.search()
        if action == "4":
            order_tool.search1()
        if action == "5":
            order_tool.change()

    elif action == "0":
        print("欢迎再次使用【航空管理系统】")
        break

    else:
        print("您输入的不正确请重新输入")
