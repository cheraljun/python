from functools import reduce
# 函数名是什么呢？函数名其实就是指向函数的变量！
f = abs # 将abs函数赋值给f, f是abs函数的函数名
print(f(-10))

# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f = abs):
    return f(x) + f(y)
result = add(-1, -2)
print(result)

L1 = [x for x in range(1, 11, 1)]
# map函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# map(函数 + 序列)
# 输出:新序列（迭代器）
def power(x):
    return x * x
whatismap = map(power, L1)
print(f'调用map函数返回的是一个迭代器, 不是具体的结果\n{whatismap}')
mapresult = list(map(power, L1))
print(f'通过list()函数让它把整个序列都计算出来并返回一个list\n{mapresult}')

# reduce函数
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(函数 + 序列)
# 输出:单一值
def pw(x, y):
    print(x, y)
    return x * y
whatisreduce = reduce(pw, L1)
print(f'调用reduce函数返回\n{whatisreduce}')

# fliter
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter() 函数接收两个参数：
# 筛选函数（返回 True 或 False）
# 可迭代对象（如列表、字符串等）
# 作用：从可迭代对象中筛选出所有让筛选函数返回 True 的元素，返回一个 迭代器（用 list() 转换为列表）。
def FL(x):
    return x % 2 == 1 # 返回布尔值

whatisfilter = filter(FL, L1)
print(f'调用filter函数返回\n{whatisfilter}')
filterresult = list(filter(FL, L1))
print(f'通过list()函数让它把整个序列都计算出来, 然后根据返回值是True还是False决定保留还是丢弃该元素。并返回一个list\n{filterresult}')

# 求素数
# 以后再学

# sorted函数
# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
rlist = [36, 5, -12, 9, -21]
print(rlist)
print(f'调用sorted函数返回: {sorted(rlist)}')

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
# 先key再sorted
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(rlist, key = abs, reverse=True))

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
