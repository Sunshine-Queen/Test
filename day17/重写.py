class Animal:
    def eat(self):
        print("------吃------")
    def drink(self):
        print("------喝------")
    def sleep(self):
        print("------睡觉------")
    def run(self):
        print("------跑------")
class Dog(Animal):
    def bark(self):
        print("------汪汪叫------")

class Xiaotq(Dog):
    def fly(self):
        print("------飞------")
    def bark(self):
        #所谓重写，就是子类中，有一个和父类相同名字的方法，
        # 在子类中的方法会覆盖掉父类中同名的方法
        print("------狂叫------")
        #第一种调用被重写的父类的方法
        Dog.bark(self)
        #第二种
        super().bark()



xiaotq=Xiaotq()
xiaotq.fly()
xiaotq.eat()
xiaotq.bark()
