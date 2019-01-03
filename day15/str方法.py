class Cat:
    """"定义了一个cat类"""
    #方法

    def __init__(self,new_name,new_age):
        self.name=new_name
        self.age=new_age

    def __str__(self):
        return"%s的年龄是:%d"%(self.name,self.age)


    def eat(self):
        print("猫正在吃鱼...")
    def drink(self):
        print("猫正在喝水...")
    def introduce(self):
        #print("%s的年龄是:%d" % (tom.name, tom.age))
        print("%s的年龄是：%d"%(self.name,self.age))


#创建一个对象
tom=Cat("汤姆",40)
lanmao=Cat("蓝猫",10)

print(tom)
print(lanmao)
