# for _ in range(3):
#     pwd = input("password: ")
#     if pwd == '8888':
#         print("login successful")
#         break
#     else:
#         print("password error")
# else:
#     print("3次输入密码错误")

a =  0
while a<3:
    pwd = input("password: ")
    if pwd == '8888':
        print("login successful")
        break
    else:
        print("password error")
        a += 1
else:
    print("3次输入密码错误")