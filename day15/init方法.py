class Cat:
    """"定义了一个cat类"""
    #方法
    #初始化对象
    def __init__(self,new_name,new_age):
        self.name=new_name
        self.age=new_age

    def eat(self):
        print("猫正在吃鱼...")
    def drink(self):
        print("猫正在喝水...")
    def introduce(self):
        #print("%s的年龄是:%d" % (tom.name, tom.age))
        print("%s的年龄是：%d"%(self.name,self.age))


#创建一个对象
tom=Cat("汤姆",40)
tom.eat()
tom.drink()
#tom.name="汤姆"
#tom.age=40
tom.introduce()


lanmao=Cat("蓝猫",10)
#lanmao.name="蓝猫"
#lanmao.age=10
lanmao.introduce()


#创建对象的过程
#1.创建一个对象
#2.Python会自动调用init方法
#3.返回创建的对象引用给tom