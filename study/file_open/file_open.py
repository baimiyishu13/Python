
stream= open(r'E:\python\config.txt',)
# r 防止转义
# mode 使用默认
# container = stream.read()
# print(container)
while True:
    a= stream.readline()
    print(a)
    if not a:
        break
# print(stream.readable())
# print(stream.readlines())