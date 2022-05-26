def input_password():
    # 1.提示用户输入密码
    pwd = input("请输入密码： ")
    # 2. 判断密码的长度是否大于8位，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3. 如果< 8主动抛出异常
    print("主动抛出异常")

    # 创建异常对象
    ex = Exception("密码长度不够")
    # 主动抛出异常
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)