# 学生管理系统v1.0

# 添加学生信息
def addStu(array):
    "添加学生信息"
    stuDict = {} #定义字典保存单个学生信息
    try:
        id = input("请输入学生学号：")
        for i in range(len(array)):
            if array[i]['id'] == id:
                print("该学号已存在，不能重复添加")
                return
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        stuDict['id'] = id
        stuDict['name'] = name
        stuDict['age'] = age
        array.append(stuDict) #把单个学生添加到总列表中
        print("添加成功")
    except BaseException:
        print("发生异常，添加失败")

# 删除学生信息
def delStu(array):
    "删除学生信息"
    try:
        id = input("请输入要删除的学生学号：")
        for i in range(len(array)):
            if array[i]['id'] == id:
               del array[i]
               return 0
        return 1
    except BaseException:
        print("发生异常，删除失败")
        return 2


# 修改学生信息
def updateStu(array):
    "修改学生信息"
    try:
        id = input("请输入要修改的学生学号：")
        for i in range(len(array)):
            if array[i]['id'] == id:
                name = input("请输入要修改的学生姓名：")
                age = input("请输入要修改的学生年龄：")
                array[i]['name'] = name
                array[i]['age'] = age
                print("修改成功")
                return
        print("找不到该学号，没法修改")
    except BaseException:
            print("发生异常，修改失败")

# 查询学生信息
def selectStu(array):
    "查询学生信息"
    try:
        id = input("请输入要查询的学生学号：")
        for i in range(len(array)):
            if array[i]['id'] == id:
                print("查询到的学生信息：",array[i])
                return
        print("查询失败，查不到该学生信息")
        return
    except BaseException:
            print("发生异常，查询失败")
            return
print("=="*30)
print("欢迎使用学生管理系统")
print("1.添加学生信息")
print("2.删除学生信息")
print("3.修改学生信息")
print("4.查询学生信息")
print("5.退出系统")
print("=="*30)
flag = 0
array = [] #定义list用于保存学生信息
while flag != 1:

    step = input("请输入你的操作：")
    try:
        step = int(step)
    except BaseException:
        print("发生异常，输入的不是数字类型")
        break
    if step == 1:
        addStu(array)
        print("学生信息打印：", array)
    elif step == 2:
        num = delStu(array)
        if num == 0:
            print("删除成功")
        elif num == 1 or num == 2:
            print("删除失败")
        print("学生信息打印：", array)
    elif step == 3:
        updateStu(array)
        print("学生信息打印：", array)
    elif step == 4:
        selectStu(array)
    else:
        flag = 1
print("退出系统成功")
