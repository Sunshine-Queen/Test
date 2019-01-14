class Tool(object):
    #属性
    num=0
    #方法
    def __init__(self,new_name):
        self.name=new_name
        Tool.num+=1#对类的属性加等于1

tool1=Tool("铁")
tool1=Tool("同")
tool1=Tool("铝")
print(Tool.num)

# 实例属性：和具体的某个实例对象有关系
# 并且一个实例对象和另外一个实例对象不共享属性
# 类属性：类属性属于类对象
# 并且多个实例之间共享一个类属性