"""
使用 open 函数操作文件
"""

with open("file.txt", "r", encoding="utf-8") as f:
     content = f.read()
     print(content)



