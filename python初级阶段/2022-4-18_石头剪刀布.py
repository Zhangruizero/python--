player = int(input("please give your choice 石头1/剪刀2/布3:"))
import random #导入随机数
computer = random.randint(1,3)#随机整数，（1，3）为闭区间

print("玩家选择的拳头是 %d-电脑的拳是 %d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player ==3 and computer == 1)):

    print("you win")
elif player == computer:
    print("平局")
else:
    print("computer win")