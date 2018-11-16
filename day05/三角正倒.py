def fun( i):
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print("")

i=1#用来控制上三角行数
#z=5放这里只出来正三角
j=1;
while i<= 5:#用来控制上三角每一行中的列数
    fun(i)
    i=i+1
i=4
while i>= 1:
    fun(i)
    i=i-1


