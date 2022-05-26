def mutable(num_list):
    num_list.append(6)
    print(num_list)


gl_list = [1, 2, 3]
mutable(gl_list)
print(gl_list)