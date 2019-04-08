def test(a,b=22,c=33):
    result=a+b+c
    print("result=%d"%result)

test(11)
test(22,33)
test(33)
#调用函数时，缺省参数的值如果没有传入，则被认为是默认值。
#带有默认值的参数一定要位于参数列表的最后面