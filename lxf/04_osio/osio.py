import os

'''
路径和目录

获取当前脚本的相对path
__file__
获取当前脚本的path 绝对路径 更保险
os.path.abspath(__file__)
拼接路径
os.path.join(os.path.dirname(os.path.abspath(__file__)), '1', '2')

获取当前工作目录
os.getcwd()

在当前工作目录创建目录（相对路径）
os.mkdir("cwd_dir")
等价于在 CWD 下创建 newdir
可能报错: FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。

最佳实践
存在则跳过，不存在则创建
os.makedirs (os.path.join(os.path.dirname(os.getcwd()), 'cwd_dir'), exist_ok=True)

获取当前脚本所在目录（绝对路径）
os.path.dirname(os.path.abspath(__file__))

在脚本所在目录创建目录（绝对路径）
可能报错: FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。
os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "script_dir"))

最佳实践
存在则跳过，不存在则创建
os.makedirs (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'script_dir'), exist_ok=True)


读文件
文本模式读（默认模式 'rt'）
with open("file.txt", "r", encoding="utf-8", errors='ignore') as f:
    content = f.read() # 读取全部内容（返回字符串）
    lines = f.readlines() # 按行读取（返回列表，每行包含换行符）           

读取大文件（逐行处理，避免内存占用）
with open("large_file.txt", "r", encoding="utf-8") as f:
    for line in f: # 逐行处理（内存友好）

二进制模式读（图片/视频等二进制文件）
读取为字节数据（bytes类型）
with open("image.png", "rb") as f:
    bytes_data = f.read()  


写文件
文本模式写（'w' 覆盖写入，文件不存在则创建）
with open("new_file.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n") # 写入字符串（自动添加换行需手动处理）
    f.writelines(["Line 1\n", "Line 2\n"]) # 写入多行列表

追加模式（'a' 在文件末尾追加内容）
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n") # 不覆盖原有内容，新增到末尾

独占创建模式（'x' 文件存在则报错）
try:
    with open("exclusive_file.txt", "x", encoding="utf-8") as f:
        f.write("Created exclusively\n")
except FileExistsError:
    print("文件已存在，创建失败")

二进制模式写（保存二进制数据）
with open("binary_data.bin", "wb") as f:
    f.write(b"\x00\x01\x02") # 写入字节数据（bytes类型）


字符编码与错误处理
指定编码并忽略错误（处理损坏的文件）
with open("corrupted.txt", "r", encoding="utf-8", errors='ignore') as f:
    content = f.read()                # 忽略无法解码的字符

显式处理编码（常见编码：utf-8, gbk, latin-1）
with open("gbk_file.txt", "r", encoding="gbk") as f:
    content = f.read()                # 按GBK编码读取
'''