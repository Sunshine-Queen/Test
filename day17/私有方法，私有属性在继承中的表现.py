class A:
    def __init__(self):
        self.num1=100
        self._num2=200
    def test1(self):
        print("-----test1------")
    def __test2(self):
        print("-----test2------")

    def test3(self):
        self.__test2()
        print(self._num2)

class B(A):
     def test4(self):
        self.__test2()
        print(self._num2)
b=B()
#b.test1()
#.__test2()私有方法不会被继承
#print(b.num1)
b.test3()
#b.test4()

# 如果调用的是 继承的父类中的 公有方法
# 可以在这个公有方法中访问父类中的私有属性和私有方法
# 但是 如果在子类中实现了一个公有方法，那么这个方法
# 是不能够调用继承父类中的私有方法和私有属性