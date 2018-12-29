def test(a,b,c=33,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
test(11,22,33,44,55,66,77,task=99,done=89)
#加**的kwargs会存放命名参数，即形如key=value的参数，kwargs为字典
