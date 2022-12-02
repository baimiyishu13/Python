class Student:
    grade = '一年级'
    def __init__(self,name,age):    # 类属性
        self.name=name      # 赋值操作
        self.age=age
    # 实例方法
    def info(self):
        print('name:',self.name,'age:',self.age)
    # 类方法
    @classmethod
    def cm(cls):
        print('类方法')
    # 静态方法
    @staticmethod
    def sm():
        print('静态方法')

stu = Student('tom',18)
print(stu.name) # 类属性   tom
stu.info()      # 类方法   name: tom age: 18

Student.info(stu)   # == stu = Student('tom',18)

print(Student.grade)
Student.cm()
Student.sm()
