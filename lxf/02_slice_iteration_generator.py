'''切片（Slice）
在 Python 里，列表切片的语法为L[start:stop:step]，其中：
start是切片起始位置，包含该位置的元素。
stop是切片结束位置，但不包含该位置的元素。
step是切片步长，默认为 1。'''

testlist = ['Ub6', 
'ght', 
'6BN', 
'Csn', 
'TlN']
testdict = {
    'pDJ': '3rD', 
    'TzB': 'IY0', 
    'BM1': 'JDo', 
    'veb': 'gx0', 
    'wFw': 'OWW'
}
print(f'原始列表，它是{testlist}')

a = testlist[0:2:1]
print(f'取出前2个元素, {a}')

a = testlist[-1]
print(f'取出倒数第1的元素, {a}')

a = testlist[-3:]
print(f'取出后3个数, {a}')

a = testlist[-3:-1]
print(f'这样只能取出排除了倒数第1个元素后的倒数2个元素, {a}')

a = testlist[::2]
print(f'每2个取一个, {a}')

'''
生成器
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
'''
La = [x for x in range(5)] # []
print(f'这是一个列表{La}')

Lb = (x for x in range(5)) # ()
print(f'这是一个列表生成器{Lb}')
print(f'第1次调用:{next(Lb)}')
print(f'第2次调用:{next(Lb)}')
print(f'第3次调用:{next(Lb)}')

'''生成器函数
首先定义一个普通函数'''
def normal_function():
    return [1, 2, 3, 4, 5]

'''
定义一个生成器函数：
生成器函数中包含 yield 关键字
当函数包含 yield 关键字时，它就不再是普通函数，而是生成器函数
调用生成器函数时，函数不会立即执行，而是返回一个生成器对象。
这里，最难理解的就是generator函数和普通函数的执行流程不一样。
普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''
def generator_function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# 调用普通函数
print(f'直接调用普通函数normal_function():{normal_function()}')

# 调用生成器函数，得到一个生成器对象
print(f'直接调用生成器函数generator_function():{generator_function()}')

'''
使用 next() 函数获取生成器的下一个值：
1. 第一次调用 next()，生成器函数开始执行，直到遇到第一个 yield 语句，此时函数暂停并返回 yield 后的值
2. 第二次调用 next()，生成器从上次暂停的 yield 处继续执行，直到下一个 yield 语句再次暂停并返回值
'''
print("生成器的第一个值:", next(generator_function()))
print("生成器的第二个值:", next(generator_function()))

'''
如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断
'''

from collections.abc import Iterable
isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代

for i in testdict: # dict's key
    print(i)
for i in testdict.values(): # dict's value
    print(i)
for i, j in testdict.items(): # dict's key & value
    print(f'key:{i}, value:{j}')

# 字符串也是可迭代对象
for str in '字符串也是可迭代对象,这是它的迭代结果':
    print(str)

'''
如果要对list实现类似Java那样的下标循环怎么办？
Python内置的enumerate函数可以把一个list变成索引-元素对，
这样就可以在for循环中同时迭代索引和元素本身
'''

for i, q in enumerate(testlist):
    print(i, q)

'''
可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象：
'''
from collections.abc import Iterator
isinstance([], Iterator)
isinstance('abc', Iterator)
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterator)
isinstance(iter('abc'), Iterator)

print(f"{isinstance([], Iterator)},{isinstance('abc', Iterator)},{isinstance(iter([]), Iterator)},{isinstance(iter('abc'), Iterator)}")

'''
你可能会问，为什么list、dict、str等数据类型不是Iterator？
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
'''
'''
有了切片操作，很多地方循环就不再需要了。Python的切片非常灵活，一行代码就可以实现很多行循环才能完成的操作。
任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
请注意区分普通函数和generator函数，普通函数调用直接返回结果：
generator函数的调用实际返回一个generator对象。
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass
实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
'''