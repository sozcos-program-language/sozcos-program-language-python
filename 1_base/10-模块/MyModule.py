"""
创建一个自定义包, 名为: my_utils
在包内提供2个模块:
1. str_utils.py
    - 函数: str_reverse(s), 接受传入字符串, 将字符串反转返回
    - 函数: substr(s, x, y), 按照下包 x 和 y, 对字符串进行切片
2. file_util.py
    - 函数: print_file_info(file_name), 接受传入文件的路径, 打印文件的全部内容, 如文件不存在则捕获异常, 输出提示信息, 通过finally关闭文件对象.
    - 函数: append_to_file(file_name, data), 接受文件路径以及传入数据, 将数据追加写入到文件中
"""

from my_utils import file_util

file_util.print_file_info('F:/projects/python-projects/sozcos/sozcos-program-language-python/1_base/10-模块/10-模块.md')

