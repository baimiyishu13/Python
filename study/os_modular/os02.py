import os
print('os.path.split:得到元组，获取路径/文件'.center(50,'*'))
path = os.path.abspath('os01.py')
result = os.path.split(path)
print(result)       # ('C:\\Users\\admin\\Desktop\\Python\\study\\os_modular', 'os01.py')
print(result[1])    # os01.py

print('os.path.splitext:得到元:获取文件后缀（类型）'.center(50,'*'))
result = os.path.splitext(path)
print(result)

print('os.path.splitext:得到元:获取文件后缀（类型）'.center(50,'*'))
result = os.path.getsize(path)
print(result)

result = os.path.dirname(path)
print(result)
