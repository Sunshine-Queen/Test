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
    """    def eat(self):
        print("------吃------")
    def drink(self):
        print("------喝------")
    def sleep(self):
        print("------睡觉------")
    def run(self):
        print("------跑------")"""

    def bark(self):
        print("------汪汪叫------")
class Cat(Animal):
    def catch(self):
        print("------抓老鼠------")
class Xiaotq(Dog):
    def fly(self):
        print("------飞------")
# a=Animal()
# a.eat
wangcai=Dog()
wangcai.eat()

tom=Cat()
tom.run()
#子类在继承的时候，在定义类时，小括号()中为父类的名字
#父类的属性、方法，会被继承给子类

xiaotq=Xiaotq()
xiaotq.fly()
xiaotq.eat()
xiaotq.bark()