# 创建文件 - 文件复制
import os

file = open(r'E:\python\a.txt',mode='w')
msg = '''
name=python
version=1.0
'''
file.write(msg)
file.close()

with open(r'E:\python\b.txt',mode='w') as file1:
    file1.write(msg)
