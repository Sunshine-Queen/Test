#1.获取要复制的文件名
old_file_name=input("请输入要复制的文件名(需要后缀):")
#2.打开要复制的文件
f_read=open(old_file_name,"r")

#假如原文名为:test.txt   ----->test[复件].txt
#尝试的版本如下
#new_file_name = old_file_name+"[复件]"
#new_file_name = old_file_name.rreplace(".","[复件].",1)

#完成新文件名
position=old_file_name.rfind(".")
new_file_name=old_file_name[0:position]+"[复件]"+old_file_name[position:]

#3.创建一个新的文件
f_write=open(new_file_name,"w")
#4.从Old文件中读取数据，写入到New文件中
#content=f_read.read()
#f_write.write(content)
while True:
    content=f_read.read(1024)
    if len(content)==0:
        break

    f_write.write(content)
#5.关闭两个文件
f_read.close()
f_write.close()