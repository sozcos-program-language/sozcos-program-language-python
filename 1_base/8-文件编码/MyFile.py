"""
使用 open 函数操作文件
"""

with open("file.txt", "r") as f:
     read = f.read()
     print(read)

with open("file.txt", "w", encoding="utf-8") as f:
     f.write("你好，世界！")






