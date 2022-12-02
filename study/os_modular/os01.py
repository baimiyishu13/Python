import os

# 绝对路径
path = os.path.dirname(__file__)    # __file__ 当前文件目录路径
print(path)

# 文件保存在当前文件目录
file_path = os.path.join(path,'a.txt')
print(file_path)

with open(r'E:\python\a.txt','r') as file1:
    container = file1.read()
    print(file1.name)   # E:\python\a.txt
    file = file1.name
    file[file.rfind('\\')+1:]
    print(file[file.rfind('\\')+1:])   # a.txt

    path = os.path.dirname(__file__)
    # file_path = os.path.join(path, 'a.txt')
    file_path = os.path.join(path, file)

    with open(file_path,'w') as file2:
        file2.write(container)

