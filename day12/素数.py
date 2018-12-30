'''#方法一

for i in range(101,201):
    a=2
    while a<i:
        if i%a==0:break
        else:a=a+1
    if a==i:
        print(i)
'''
#方法二
list=[]
for i in range(101,201):
    q=i
    j=2
    while j<q:
        if i%j==0:break
        else:
            q=i//j
            j=j+1
    else:
        list.append(i)
print(list)
