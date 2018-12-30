def test(a,b,func):
    result=func(a,b)
    print(result)

func_new=input("请输入一个匿名函数：")
func_new=eval(func_new)
test(11,22,func_new)
#python3里面把输入的东西都当成字符串，而eval即去掉“”，用来计算在字符串中有效的Python表达式