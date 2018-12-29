#4！=4*3*2*1
#5！=5*4*3*2*1
'''i=1
result=1
while i<=4:
    result=result*i
    i+=1
print(result)
'''

def calNum(num):
    if num>=1:
     result=num * calNum(num-1)
    else:
        result=1
    return result
ret=calNum(3)
print(ret)
