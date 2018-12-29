#有时可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，声明时不会命名
def sum_2_nums(a,b,*args):
    print("-"*30)
    print(a)
    print(b)
    print(args)

    #result=a+b
    #print("result=%d"%result)

    result=a+b
    for num in args:
        result+=num
        print("result=%d"%result)

sum_2_nums(11,22,33,44,55,66,77)#加了星号（*）的变量args会存放所有未命名的变量参数，args为元组
sum_2_nums(11,22,33)
sum_2_nums(11,22)
sum_2_nums(11)#错误,因为形参中至少要有两个实参