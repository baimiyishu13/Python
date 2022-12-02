# Library management system
msg = '''
                       **********************************************************
                                   Welcome to Library management system !
                       **********************************************************
                        1. 注册用户
                        2. 用户登录 
                        3. 图书列表
'''
print(msg)
opt = input('请选择（编号）:')



# 注册
def user_register():
    print('用户注册'.center(20,'-'))
    username = input('username:')
    password = input('password:')
    repassword = input('repassword:')

    if password == repassword:
        # 保存信息
        with open('user.txt','a') as passwd:
            passwd.write('{} {}\n'.format(username,password))
        # 打印用户注册成功
        print('注册成功')
    else:
        print('注册失败，密码不一致')

# 登录
def user_login():
    print('用户登录'.center(20,'-'))
    username = input('username:')
    password = input('password:')
    # 判断user和password不为空
    if username and password:
        with open('./user.txt','r') as rstream:
            while True:
                # 读一行
                user= rstream.readline()
                if not user:
                    print('用户名或密码错误')
                    break
                input_user = '{} {}\n'.format(username,password)
                if user == input_user:
                    print('登录成功')
                    break
# 图书
def show_books():
    print('书架'.center(20, '-'))
    with open('./books.txt','r') as rstream:
        # books = rstream.readlines()
        books = rstream.readlines()
        for book in books:
            print(book,end='')

# 主程序
if opt == '1':
    user_register()
elif opt == '2':
    user_login()
elif opt == '3':
    show_books()
else:
    print('输入错误')
