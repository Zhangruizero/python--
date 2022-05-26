name_list = ["张三", "李四", "王五", "王小二", "张三"]
# len 函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含了%d个元素" % list_len)

# count 方法可以统计列表中某个数出现的次数
count = name_list.count("张三")
print(count)