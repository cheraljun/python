'''
为什么需要装饰器？装饰器的主要用途有：
代码复用：避免相同的辅助性代码在多个函数中重复 
分离关注点：将核心逻辑与辅助功能(如日志、计时等)分离动态增加功能：
不改动原函数代码的情况下增加新功能可读性：使代码结构更清晰，意图更明确
'''
def funclog(func): # 将函数赋值给变量func
    def wrapper(): # wrapper包裹了原函数func，并在其前后添加了额外的代码。
        print(f'正在调用{func.__name__}...')
        func() # 调用func函数
        print(f'{func.__name__}执行成功!')
    return wrapper

@funclog # 等价于 sayhello = funclog(sayhello)
def sayhello():
    print('你好')

sayhello() # 实际上调用的是 wrapper()

'''
万能装饰器
这三个步骤是装饰器的核心逻辑，确保了：
接收原函数：通过外层函数参数 func 接收被装饰的函数
处理参数：通过 *args, **kwargs 捕获并传递所有参数
处理返回值：保存并返回原函数的返回结果，保持函数行为一致
这种结构可以无缝适配任何函数，无论其参数类型或是否有返回值。
'''
def decorator(func):  # 1. 接收原函数作为参数
    def wrapper(*args, **kwargs):  # 2. 用*args和**kwargs处理原函数的所有参数
        result = func(*args, **kwargs)  # 调用原函数并传递参数，保存返回值
        return result  # 3. 返回原函数的返回值
    return wrapper  # 返回包装函数，替代原函数