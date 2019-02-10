try:
    open("xxx.txt")
    print("------1--------")

except NameError:
    print("如果捕获到异常后做的处理。。。")

except FileNotFoundError:
    print("文件不存在。。。")

print("-------2---------")