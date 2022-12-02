import os

# 绝对路径
r = os.path.isabs(r'E:\python\a.txt')
print(r)

# 相对路径，操作方便
print('相对路径'.center(40,'-'))
r = os.path.isabs('os_modular/a.txt')
print(r)    # False
# 当前文件的上一级 ..
r = os.path.isabs('../file_open/file_copy.py')
print(r)    # False

# 当前 目录文件夹 名字
print('文件所在文件夹'.center(40,'-'))
path = os.path.dirname(__file__)    # C:\Users\admin\Desktop\Python\study\os_modular
print(path)

# 通过相对路径得到绝对路径
print('获取文件绝对路径'.center(40,'-'))
path = os.path.abspath('a.txt')     # C:\Users\admin\Desktop\Python\study\os_modular\a.txt
print(path)

# 当前文件的绝对路径
# 方法一：__file__
print('当前文件的工作目录'.center(40,'-'))
path = os.getcwd()  # C:\Users\admin\Desktop\Python\study\os_modular
print(path)