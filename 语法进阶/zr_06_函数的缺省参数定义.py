def print_info(name, gender=True):
    """

    :param name: 班上同学的姓名
    :param gender: True为男生false为女
    """
    gender_test = "man"
    if not gender:
        gender_test = "women"
    print("%s 是 %s" % (name, gender_test))


print_info("小明")
print_info("老王")
print_info("小美", False)