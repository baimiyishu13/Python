# 可迭代对象 string
import datetime

for item in "100":
    print(item,type(item))


# range() 产生一个整数序列，可迭代的对象
for i in range(10):
    print(i)

for _ in range(5):
    print("少时春风马蹄疾，不知人间有别离")

sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
print(sum)

# 100 到 999 的水仙花数
for i in range(100,1000):
    ge = i % 10
    shi = i //10 % 10
    bai = i // 100
    if i == (ge**3+shi**3+bai**3):
        print(i)
    else:
        print("hah")
