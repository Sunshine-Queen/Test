def fun():
    year = int(input("你输入一个年份，我告诉你它是否是闰年:"))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("您输入的年份[%d]是闰年" % year)

    else:
        print("您输入的年份（%d）不是闰年" % year)


fun()