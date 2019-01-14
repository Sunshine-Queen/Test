class Game(object):

    #类属性
    num=0

    #实例方法
    def __init__(self):
        #实例属性
        self.name="laowang"

    #类方法
    @classmethod
    def add_num(cls):
        cls.num=100

    #静态方法
    @staticmethod
    def print_num():
        print("--------------")
        print("      穿越火线V11,1")
        print(" 1.开始游戏")
        print(" 2.结束游戏")
        print("-------------")

game=Game()
#Game.add_num()#可以通过类的名字调用方法
game.add_num()#还可以通过这个类创建出来的对象 去调用这个方法
print(Game.num)

#Game.print_num()#通过类调用静态方法
game.print_num()#通过实例对象调用静态方法