import os
#1.获取一个要重命名的文件夹的名字
folder_name=input("请输入要重命名的文件夹的名字：")

#2.获取那个文件夹里面所有文件的名字
file_names=os.listdir(folder_name)
#第一种的方法
os.chdir(folder_name)

#3.对获取的名字进行重命名
for name in file_names:
    print(name)
    os.rename(name,"[活着]-"+name)