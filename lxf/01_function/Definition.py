'''
定义函数
在Python中, 定义一个函数要使用def语句, 
依次写出函数名、括号、括号中的参数和冒号:
还有函数的return值
我老婆多大函数,添加输入错误后重新输入的功能。

错误处理try-except语句
在 Python 中, 异常处理是一种重要的机制, 用于捕获和处理程序运行过程中可能出现的错误情况。
try-except 语句是实现异常处理的主要方式。其基本结构如下：
try:
    这里放置可能会抛出异常的代码块。当这些代码执行时, 如果出现了异常, 
    程序会立即停止执行 try 块中的后续代码, 并跳转到对应的 except 块进行处理。
except ExceptionType:
    这里的 ExceptionType 是要捕获的异常类型。当 try 块中抛出的异常类型与之匹配时, 
    就会执行 except 块中的代码, 通常用于处理异常或输出错误信息。
    可以有多个 except 块, 用于捕获不同类型的异常, 也可以使用一个通用的 except 块（如 except Exception）
    来捕获所有类型的异常, 但在实际应用中, 尽量明确指定要捕获的异常类型, 以提高代码的可读性和调试性。
'''
def wifeage():
    print('欢迎使用: 计算老婆年龄函数')
    count = 0
    # 开启一个无限循环, 该循环会持续运行, 直到满足特定条件（如使用 break 或 return 语句）跳出循环
    # 这里的目的是持续提示用户输入, 直到输入正确答案
    while True:
        try:
            year = int(input('今年是几几年？'))
            age = year-2003
            count = count + 1
            print('数据正确!')
            if age >= 0:
                print(f'函数调用成功!\n我老婆出生{age}年啦~!\n结束函数的执行!\n')
                # 输入正确后, 使用 return 语句返回当前年龄, 同时结束函数的执行
                # 由于函数结束, while 循环也会随之终止
                return age
            else:
                print(f'第{count}次尝试。不过这时候我老婆还没出生呢。。')
        except Exception as e:
            # 若在 try 块中的代码执行时出现异常, 比如用户输入的不是有效的整数
            # int() 函数在转换时会抛出 ValueError 异常, 或者出现其他类型的异常
            # 程序会跳转到 except 块进行异常处理
            # 变量 e 是捕获到的异常对象, 它包含了异常的相关信息, 如异常类型、错误消息等
            # 打印异常提示信息, 提醒用户仔细查看后重新输入
            print(f'数据不对, 看清楚再重来: {e}')
wifeage()

'''
返回多个值的函数, Python的函数返回多值其实就是返回一个tuple
'''
def double():
    print('欢迎使用:double函数!请输入3个整数')
    while True:
        try:
            x = int(input('x=?'))
            y = int(input('y=?'))
            z = int(input('z=?'))
            print('正在检查数据...')
            print(f'输入正确!正在调用double函数...\n您输入了{x}, {y}, {z}')
            x2 = x * 2
            y2 = y * 2
            z2 = z * 2
            print(f'函数调用成功!\n正在分别计算{x}, {y}, {z}的2倍...\n{x}, {y}, {z}的2倍分别为{x2}, {y2}, {z2}!\n结束函数的执行!\n')
            return(x, y, z)
        except Exception as e:
            print(f'???输入的啥?重来!看清楚可用的数据类型: {e}')
print(f'这是函数的返回值{double()}')

'''
空函数
'''
def nothing():
    print('正在调用空函数, 此函数不执行\n结束函数的执行!\n')
    pass
nothing()

'''
递归函数
'''
def factorial(x):
    # 递归终止条件
    if x == 1:
        return 1
    # 递归调用
    result = x * factorial(x - 1)
    return result
print(factorial(10))