try:
    open("xxx.txt")
    print("-----1-----")
except(NameError,FileNotFoundError):
    print("如果捕获到的异常后做的。处理、")
print("------2------")