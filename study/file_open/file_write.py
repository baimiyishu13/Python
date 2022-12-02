# 追加和写操作

file = open(r'E:\python\config.txt',mode='a')
# mode 写

mysql_config = '''
user=mysql
password=mysql@123
'''
modify_file = file.write(mysql_config)

# 需要加换行
file.writelines(['worddir=/opt/mysql\n','databases=containers'])

# 关闭通道
file.close()

