try:
    11/0
    open("xxx.txt")
    print("-----1-----")
except(NameError,FileNotFoundError):
    print("如果捕获到异常后做的，处理。")
except Exception:
    print("如果用了Exception，那么意味着只要上面的except没有捕获到异常，这个excep"
          "一定会捕获到")
print("-----2----")