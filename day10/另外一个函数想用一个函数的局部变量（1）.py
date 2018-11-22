def get_wendu():
    wendu=33
    return wendu

def print_wendu(wendu):
    print("温度是%d"%wendu)
result=get_wendu()#如果一个函数有返回值，但是在没有调用函数之前用变量保存的话，那么没有任何的意义
print_wendu(result)
