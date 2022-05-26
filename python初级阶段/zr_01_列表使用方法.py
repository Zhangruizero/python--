name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list[2])

# index 搜索所需要的数据在数组中的位置
print(name_list.index("wangwu"))

# 修改
name_list[1] = "李斯"

# append 可以向列表末尾追加数据
name_list.append("wangler")

# insert 在所给位置插入
name_list.insert(1, "xiaomeimei")

# entend 可以把其它列表中的完整内容， 追加到当前列表的末尾
temp_list = ["孙悟空", "猪八戒", "沙师弟"]
name_list.extend(temp_list)
print(name_list)

# remove 可以从列表中删除指定数据
name_list.remove("wangwu")

# pop 默认弹出最后一个元素
name_list.pop()
name_list.pop(3)

# clear 可以删除表中所有数据
name_list.clear()
print(name_list)