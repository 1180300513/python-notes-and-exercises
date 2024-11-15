# def 函数名(参数列表):
#     函数体
#     return 返回值（可选）
from docutils.nodes import address


def show_person_info(name,age=11):
    print(f"名字:{name},年龄:{age}")

show_person_info('张三',30)
show_person_info('张四')
show_person_info(age=30,name='张五')


def show_person_info(name,age=11,address='桥洞',sex='非人'):
    print(f"名字:{name},年龄:{age},住址:{address},性别:{sex}")

show_person_info('李四',address='马路')
