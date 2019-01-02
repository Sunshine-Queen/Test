import os

#1. 获取一个要重命名的文件夹的名字
folder_name =  input("请输入要重命名的文件夹:")

#2. 获取那个文件夹中所有的文件名字
file_names = os.listdir(folder_name)

#第1中方法
#os.chdir(folder_name)

#3. 对获取的名字进行重命名即可
#for name in file_names:
#    print(name)
#    os.rename(name,"[活着]-"+name)



for name in file_names:
    #print(name)
    old_file_name = "./"+ folder_name + "/" +name
    new_file_name = "./"+folder_name+"/"+"[活着]-"+name
    os.rename(old_file_name, new_file_name)
