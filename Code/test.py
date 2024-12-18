# class 类名:
# 属性
# 方法
#
# 1.命名规范：       类名的首字母大写
# 2.创建对象：       对象名 = 类名（参数）
# 3.使用属性、方法：  对象名.属性名(方法名)


class Student:
    name = '小花'
    age = 15
    sex = '女'

    def __init__(self,name='小花'):
        self.name = name
    def eat(self):
        print("{}在吃东西".format(self.name))
    def fun(self,message):
        print("有人对{}留言了，内容为:{}".format(self.name,message))

class XiaoHua(Student):
    def sleep(self):
        print("{}睡着了".format(self.name))

s1 = Student()
s1.eat()
s1.fun("你在干什么?")

s2 = Student('小芳')
s2.eat()
s2.fun("睡了么?")

s3 = XiaoHua("小华")
s3.eat()
s3.sleep()