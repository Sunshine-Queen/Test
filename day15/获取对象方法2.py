class Cat:
    #属性

    #方法
    def eat(self):
        print("猫正在吃鱼...")
    def drink(self):
        print("猫正在喝水...")
    def introduce(self):
        print("%s的年龄是:%d" % (tom.name, tom.age))
#创建一个对象
tom=Cat()
#调用tom指向对象中的方法
tom.eat()
tom.drink()
#给tom指向的对象添加两个属性
tom.name="汤姆"
tom.age=40

#print("%s的年龄是:%d" %(tom.name,tom.age))
tom.introduce()

#有错误
lanmao=Cat()
lanmao.name="蓝猫"
lanmao.age=10
lanmao.introduce()