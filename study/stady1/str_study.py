a = 'Python'
b = "Python"
c = '''Python'''
print(a,id(a))      # Python 140705909475288
print(b,id(b))      # Python 140705909475288
print(c,id(c))      # Python 140705909475288

s = 'Hello world'


print(s.center(20,))
print(s.ljust(20,'*'))  # Hello world*********
print(s.rjust(20,'-'))  # ---------Hello world
print(s.zfill(20,))
print(s.center(40,'-')) # --------------Hello world--------------

print(s.split())            # ['Hello', 'world']
print(s.split(sep='o'))     # ['Hell', ' w', 'rld']
print(s.split(sep='o',maxsplit=1))  # ['Hell', ' world'] 劈分一次

print(s.isalnum())
print(s.isnumeric())



s = 'A,B,C,A'
print(s.replace('A','M',2)) # M,B,C,M

lst = ['/etc','/passwd',]
print(''.join(lst))         # /etc/passwd


name = 'tom'
age = 18
# 打印出 ： 姓名：tom,年龄：18
print('姓名：%s 年龄：%d' %(name,age))    # 姓名：tom 年龄：18

print('姓名：{0} 年龄：{1}'.format(name,age)) # 姓名：tom 年龄：18



