money=int(input("请输入你的公交卡当前余额："))
number=int(input("请输入你看到的有的空座位个数："))
if money >= 2:
    print("亲爱的乘客，你可以上车啦...")
    if number > 0:
        print("你可以坐下了...")
    else:
        print("你可以上车，但是你没有座位可以坐")
else:
    print("您的余额不足。")