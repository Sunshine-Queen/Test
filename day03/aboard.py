ticket=1#1表示有车票，0表示没有车票
knifeLength=12#cm

#先判断是否有车票
if ticket == 1:
    print("有车票，可以进站")

    #判断刀的长度是否合法
    if knifeLength <=10 :
        print("通过安检")
        print("终于可以见到Ta了，美滋滋~~~")

    else:
        print("没有通过安检")
        print("刀子的长度超过规定，等待警察处理...")
else:
    print("没有车票，不能进站")
    print("快去买票吧")
