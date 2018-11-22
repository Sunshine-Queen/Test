nums=[11,22,33]
infor = {"name":"laowang"}
def test():
    nums.append(44)
    infor['age']=10

def test2():
    print(nums)
    print(infor)
test()
test2()
#列表字典可以直接对全局变量进行修改