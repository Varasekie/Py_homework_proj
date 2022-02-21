class student:
    # 可以规定count为stu的类的私有类属性
    # 当然也可以只是规定为类属性
    __count = 0

    # 初始化，每多一个学生，类的count属性就会+1
    def __init__(self, age, name, sex):
        self.age = age
        self.name = name
        self.sex = sex
        student.__count = student.__count + 1

    # 可以定义静态方法，获取学生的私有类属性count
    @staticmethod
    def getCount():
        print('学生的数量为',student.__count)


aStu = student(6, 'cly', '女')
bStu = student(10, 'ly', '男')
student.getCount()
