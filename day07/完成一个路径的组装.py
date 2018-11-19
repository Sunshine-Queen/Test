#完成一个路径的组装
import os
path1 = input("请输入主路径：")
path2 = input("请输入路径2：")
path3 = input("请输入路径3：")
path = os.path.join(path1, path2, path3)
print("输出路径:", path)
