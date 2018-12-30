for m in range(1,10):
    for n in range(1,10):
        if m >= n:#1×2=2 和 2×1=2 这些乘积相同的式子，我们可以使用if语句对结果进行限制
            print('%s×%s=%s'%(m,n,m*n),end=' ')
        #end=''阻止换行 成了一行
    print()#第二个print的缩进，跟第二个for齐平。需要多行多列，可以用一个空print消掉end来实现

