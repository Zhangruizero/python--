def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)
gl_dict = {"name": "小美", "age ": 19}
# 拆包语法
demo(*gl_nums, **gl_dict)
# demo(1, 2, 3, name="小美", age= 19)
