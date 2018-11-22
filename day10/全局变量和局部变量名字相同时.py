a=300
def test1():
    a=100
    print("------test1---修改前----a=%d"%a)
    a=200
    print("------test1---修改后----a=%d"%a)

def test2():
    print("------test3---修改----a=%d"%a)

test1()
test2()
#如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的