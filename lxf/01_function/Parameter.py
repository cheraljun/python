'''
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''

# 位置参数
def power(x):
    xx = x ** 2
    print(f'位置参数函数测试, 乘方函数调用成功, 数字{x}的乘方是{xx}')
power(6)

# 默认参数
# 必选参数在前，默认参数在后，否则Python的解释器会报错
def multiply(x, y = 10):
    xy = x ** y
    if y == 10:
        print(f'默认参数函数测试, 相乘函数调用成功, 调用默认值, y = {y}, 数字{x}的{y}次方是{xy}')
    else:
        print(f'默认参数函数测试, 相乘函数调用成功, 覆盖默认值, y = {y}, 数字{x}的{y}次方是{xy}')
    return xy
multiply(6)
multiply(6, 6)

# 可变参数
# *args是可变参数，args接收的是一个tuple
def infinitemultiply(*args):
    result = 1
    for arg in args:
        result = arg * result
    print(f'可变参数函数测试, 无限制相乘函数调用成功, {args}中的数字相乘后是{result}')
    return result
infinitemultiply(1, 2, 3, 4)

testlist = ['Ub6', 
'ght', 
'6BN', 
'Csn', 
'TlN']
def TESTLIST(*args):
    print('可变参数可以先组装list或tuple，再通过*args传入')
    for arg in args:
        print(f'组装list或tuple，再通过*args传入示例{arg}')
TESTLIST(*testlist)

# 关键字参数
# **kw是关键字参数，kw接收的是一个dict
def keywordparameter1(**kw):
    print(f'关键字参数函数测试, 关键字参数函数调用成功\n{kw}')
keywordparameter1(关键字参数key1 = '关键字参数value, 字符串', 关键字参数key2 = 99, 关键字参数key3 = [1, 2, 3, 4])

# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 例如，只接收name和city作为关键字参数。这种方式定义的函数如下：
def keywordparameter2(*, name, city):
    print(f'命名关键字参数函数测试, 命名关键字参数函数调用成功\n{name}\n{city}')
keywordparameter2(name = 'jun', city = 'guangzhou')
'''
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
keywordparameter2()
Traceback (most recent call last):
  File "c:/Users/admin/Desktop/jun/python/lxf/01_function/Parameter.py", line 41, in <module>
    keywordparameter2()
TypeError: keywordparameter2() missing 2 required keyword-only arguments: 'name' and 'city'
'''

'''
函数定义：TESTDICT 函数使用 **kw 这种可变关键字参数来接收任意数量的关键字参数，这些参数会被打包成一个字典。
遍历键值对：在函数内部，使用 kw.items() 方法获取字典 kw 的所有键值对视图，然后通过 for 循环将每个键值对解包为 key 和 value 变量，最后打印出键和值。
函数调用：使用 **testdict 对字典 testdict 进行解包，将其键值对作为关键字参数传递给 TESTDICT 函数。
'''
testdict = {
    'pDJ': '3rD', 
    'TzB': 'IY0', 
    'BM1': 'JDo', 
    'veb': 'gx0', 
    'wFw': 'OWW'
}
def TESTDICT(**kw):
    print('关键字参数可以先组装dict，再通过**kw传入')
    for key, value in kw.items():
        print(f'组装dict，再通过**kw传入示例键: {key}, 值: {value}')
TESTDICT(**testdict)