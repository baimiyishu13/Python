def add(a=10,b=20):
    c = print(a+b)  # c 称为：局部变量
    return c

add()   # 30

# 函数体外定义
a = 100
def fun():
    global c
    c = 99
    print(a)    # 内外都可以使用
fun()
print(c)