class Cat:
    #属性

    #方法
    def eat(self):
        print("猫正在吃鱼...")
    def drink(self):
        print("猫正在喝水...")
    def introduce(self):
        #print("%s的年龄是:%d" % (tom.name, tom.age))
        print("%s的年龄是：%d"%(self.name,self.age))

        #所谓的self，可以理解为自己
        #某个对象调用其方法时，python解释器会把这个对象作为第一个参数传递给self，所以开发者只需要传递后面的参数即可
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


lanmao=Cat()
lanmao.name="蓝猫"
lanmao.age=10
lanmao.introduce()