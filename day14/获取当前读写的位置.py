# 打开一个已经存在的文件
f = open("heihei.txt", "r")
str = f.read(3)
print("读取的数据是 : ", str)

# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)


f.close()


#如果在读写文件的过程中，需要从另外一个位置进行操作的话，可以使用seek()


#seek(offset, from)有2个参数
#offset:偏移量
#from:方向
#0:表示文件开头
#1:表示当前位置
#2:表示文件末尾
