def test():
    a=11
    b=22
    c=33

    #用一个列表来封装3个变量的值
    d=[a,b,c]
    #return b
    #return c
    # return d
    #return [a,b,c]
    #return (a,b,c)
    return  a,b,c#默认封装成一个元祖
num=test()
print(num)
