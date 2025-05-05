# 欢迎来到这个Python基础学习项目！本项目将带领你逐步了解Python的基础知识，别着急，我们会一步一个脚印地学习。

# 1. 简介
# Python是一种高级编程语言，以其简洁易读的语法而闻名，广泛应用于数据科学、机器学习、Web开发等领域。
# 这个项目的目标是帮助你从零基础开始，掌握Python的基本概念和操作。

# 2. Python基础

# 2.1 字符串和输出
# 单引号或者双引号括起来的文本叫做字符串
# 使用 print() 函数可以将字符串输出到控制台
print('示例开始：使用单引号和双引号输出字符串')
print('hello world')
print("hello world")
print('示例结束：使用单引号和双引号输出字符串')

# print() 函数可以接受多个字符串，用英文逗号“,”隔开，输出时字符串之间会有一个空格
print('示例开始：使用 print() 函数输出多个字符串')
print('hello world', 'cheral chen')
print('示例结束：使用 print() 函数输出多个字符串')

# print() 函数也可以打印整数，或者计算结果
print('示例开始：使用 print() 函数打印整数和计算结果')
print(300)
print(100 + 200)
print('示例结束：使用 print() 函数打印整数和计算结果')

# 2.2 输入
# Python提供了 input() 函数，可以让用户输入字符串，并将其存放到一个变量里
print('示例开始：使用 input() 函数获取用户输入并输出')
name = input('your wife叫什么？')
print('your wife named', name)
print('示例结束：使用 input() 函数获取用户输入并输出')

# 2.3 变量
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# 等号 = 是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
print('示例开始：变量的定义和赋值')
a = 1
mywife = 'cheralchen'
Answer = True

# 变量 a 先赋值为整数
print(a)
# 变量 a 再赋值为字符串
a = 'ABC'
print(a)
print('示例结束：变量的定义和赋值')

# 2.4 常量
# 所谓常量就是不能变的变量，在Python中，通常用全部大写的变量名表示常量
print('示例开始：定义和使用常量')
PI = 3.14159265359
print(PI)
print('示例结束：定义和使用常量')

# 2.5 空值
# 空值是Python里一个特殊的值，用 None 表示。None 不能理解为 0，因为 0 是有意义的，而 None 是一个特殊的空值

# 2.6 条件判断
# Python的语法比较简单，采用缩进方式。当语句以冒号: 结尾时，缩进的语句视为代码块
# 条件判断用 if 语句实现，如果 if 判断是 False，就不执行这个if语句下的缩进，继续执行 else 语句块中的内容，如果没有 else 就跳过。
# elif 是 else if 的缩写，完全可以有多个 elif
print('示例开始：使用 if 语句进行条件判断')
if 1 > 0:
    print('haha,1>0')
print('示例结束：使用 if 语句进行条件判断')

# 2.7 数据类型

# 2.7.1 整数
# 整数是Python中的基本数据类型之一
print('示例开始：打印整数')
print(100)
print('示例结束：打印整数')

# 2.7.2 浮点数
# 浮点数是带有小数点的数字
print('示例开始：打印浮点数')
print(9.9)
print('示例结束：打印浮点数')

# 2.7.3 字符串
# 字符串是以单引号'或双引号"括起来的任意文本
print('示例开始：使用单引号和双引号输出字符串')
print('hello')
print("hello!")
print('示例结束：使用单引号和双引号输出字符串')

# 如果字符串本身包含单引号，可以用双引号括起来
print('示例开始：字符串包含单引号时使用双引号括起来')
print("hello'cheralchen'")
print('示例结束：字符串包含单引号时使用双引号括起来')

# 字符串内部既包含'又包含"，用转义字符 \' 来标识'
# 转义字符 \ 可以转义很多字符，比如 \n 表示换行，\t 表示制表符，字符 \ 本身也要转义，所以 \\ 表示的字符就是 \
# r'' 表示 '' 内部的字符串默认不转义
print('示例开始：使用转义字符和原始字符串')
print('\'这是单引号\'\"这是双引号\"')
print("\'这是单引号\'\"这是双引号\"")
print('\'这是单引号\'')
print('第一行\n这是第二行:换行了')
print('\t制表')
print('这是一个斜杠:\\')
print(r'\n换行无效')
print('示例结束：使用转义字符和原始字符串')

# 如果字符串内部有很多换行，用三个单引号引用的格式表示多行内容
print('示例开始：使用三个单引号表示多行字符串')
print('''line1
line2
line3
line4
line5''')
print(r'''line1\n
line2
line3
line4
line5''')
print('示例结束：使用三个单引号表示多行字符串')

# 2.7.4 字符串格式化
# 格式化用 % 实现
# %s 表示用字符串替换，%d 表示用整数替换，%f 表示浮点数，%% 来表示一个 %
# 有几个 %? 占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个 %?，括号可以省略
print('示例开始：使用 % 进行字符串格式化')
print('I have %d cats named %s, %s, %s' % (3, 'miaomiao', 'hei', 'sanmiao'))
print('示例结束：使用 % 进行字符串格式化')

# 还有一种格式化字符串的方法是使用以 f 开头的字符串，称之为 f-string
# 它和普通字符串不同之处在于，字符串如果包含 {xxx}，就会以对应的变量替换
print('示例开始：使用 f-string 进行字符串格式化')
wifename = 'cheralchen'
wifecount = 1
print(f'我老婆是{wifename}, 我有{wifecount}个老婆')
print('示例结束：使用 f-string 进行字符串格式化')

# 练习
# 小明的成绩从去年的72分提升到了今年的85分，计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
print('示例开始：计算成绩提升率并进行字符串格式化')
lyscore = 72
tyscore = 85
up = ((tyscore - lyscore) / lyscore) * 100

# f-string 格式化
print(f'debug...去年成绩{lyscore},今年成绩{tyscore},提升率为{up:.1f}%')
# 传统 % 格式化
print('debug...去年成绩%d,今年成绩%d,%.1f%%' % (lyscore, tyscore, up))
print('示例结束：计算成绩提升率并进行字符串格式化')

# 2.8 列表（list）
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素

print('示例开始：创建和查看列表')
friends = ['cheralchen', 'ruikang']
print(friends)
print('示例结束：创建和查看列表')

print('示例开始：获取列表元素个数')
print(len(friends))
print('示例结束：获取列表元素个数')

print('示例开始：使用索引访问列表元素')
# 列表的索引从 0 开始
print(friends[0])
print(friends[1])
print('示例结束：使用索引访问列表元素')

print('示例开始：在列表末尾添加元素')
# append() 方法可以在列表末尾添加一个元素
friends.append('bo')
print(friends)
print('示例结束：在列表末尾添加元素')

print('示例开始：在指定位置插入元素')
# insert() 方法可以在指定位置插入一个元素
friends.insert(1, 'jingxuan')
print(friends)
print('示例结束：在指定位置插入元素')

print('示例开始：删除列表元素')
# 删除末尾元素
# pop() 方法如果不指定索引，默认删除列表末尾的元素
friends.append('test1')
print(friends)
friends.pop()
print(friends)
# 删除指定位置元素
# pop() 方法如果指定索引，会删除该索引位置的元素
friends.insert(0, 'test2')
print(friends)
friends.pop(0)
print(friends)
print('示例结束：删除列表元素')

print('示例开始：修改列表元素')
# 可以通过索引直接修改列表中的元素
friends[0] = 'mywife'
print(friends)
print('示例结束：修改列表元素')

print('示例开始：列表元素的数据类型可以不同')
L = ['Apple', 123, True]
print(L)
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(len(s))
# 拿到 'php'
print(s[2][1])
print('示例结束：列表元素的数据类型可以不同')

print('示例开始：创建空列表')
L = []
print(L)
print(len(L))
print('示例结束：创建空列表')

# 2.9 元组（tuple）
# 另一种有序列表叫元组：tuple。tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改
print('示例开始：创建和查看元组')
turplefriends = ('cheralchen', 'ruikang')
print(turplefriends)
print(turplefriends[0])
print('示例结束：创建和查看元组')

print('示例开始：创建空元组')
t1 = ()
print(t1)
print('示例结束：创建空元组')

# 只有 1 个元素的 tuple 定义时必须加一个逗号,，来消除歧义
print('示例开始：创建只包含一个元素的元组')
t2 = (1,)
print(t2)
print('示例结束：创建只包含一个元素的元组')

# 练习
# 用索引取出下面 list 的指定元素
print('示例开始：使用索引取出嵌套列表中的元素')
fruit = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印 Apple
print(fruit[0][0])
# 打印 Python
print(fruit[1][1])
# 打印 Bob
print(fruit[2][2])
print('示例结束：使用索引取出嵌套列表中的元素')

# 2.10 条件判断再议
# input() 返回的数据类型是 str，str 不能直接和整数比较，必须先把 str 转换成整数。Python 提供了 int() 函数来完成这件事情
print('示例开始：使用 if-elif-else 进行年龄判断')
age = 3
if age >= 18:
    print(f'adult, your age is {age}')
elif age >= 6:
    print(f'teenager, your age is {age}')
else:
    print(f'kid, your age is {age}')
print('示例结束：使用 if-elif-else 进行年龄判断')

print('示例开始：根据用户输入的出生年份进行判断')
birth = input('几几年出生: ')
try:
    print(f'已获取用户输入:{birth}, 正在调用\'根据用户输入的出生年份进行判断\'示例')
    birth = int(birth)
    if birth < 2000:
        print('00前')
    else:
        print('00后')
except Exception as e:
    print(f'调用\'根据用户输入的出生年份进行判断\'示例出现报错, 报错为{e}')
print('示例结束：根据用户输入的出生年份进行判断')

print('示例开始：简单的数学计算')
n = 1 + 2 + 3
print(n)
print('示例结束：简单的数学计算')

# 2.11 循环
# Python的循环有两种

# 2.11.1 for...in 循环
# 依次把 list 或 tuple 中的每个元素迭代出来
print('示例开始：使用 for...in 循环遍历列表')
friends = ['cheralchen', 'ruikang']
for friend in friends:
    print(friend)
print('示例结束：使用 for...in 循环遍历列表')

print('示例开始：使用 for...in 循环计算 1 - 100 的整数之和')
x = 0
for n in range(101):
    x = x + n
print(x)
print('示例结束：使用 for...in 循环计算 1 - 100 的整数之和')

# 2.11.2 while 循环
# 只要条件满足，就不断循环，条件不满足时退出循环
print('示例开始：使用 while 循环')
x = 9
while x == 9:
    print('x为9')
    break
print('示例结束：使用 while 循环')

print('示例开始：使用 for...in 循环对列表中的每个名字打印出 Hello, xxx!')
L = ['Bart', 'Lisa', 'Adam']
for boy in L:
    print(f'hello,{boy}')
print('示例结束：使用 for...in 循环对列表中的每个名字打印出 Hello, xxx!')

# 2.11.3 break 和 continue 语句
# break 的作用是提前结束循环
print('示例开始：使用 break 语句提前结束循环')
x = 0
for n in range(101):
    x = x + n
    if x >= 100:
        break
print(x)
print('示例结束：使用 break 语句提前结束循环')

# continue 语句，跳过当前的这次循环，直接开始下一次循环
print('示例开始：使用 continue 语句跳过特定的循环')
# 打印 0 - 6，不打印 1 和 2
for x in range(7):
    if x == 1 or x == 2:
        continue
    else:
        print(x)
print('示例结束：使用 continue 语句跳过特定的循环')

# 2.12 字典（dict）
# dict 就像一个字典，每个键（key）都有对应的解释（值，value）
print('示例开始：创建和访问字典')
mycore = {'wife': 'cheralchen', 'friend': 'ruikang'}
print(mycore['wife'])
print('示例结束：创建和访问字典')

print('示例开始：向字典中添加元素')
mycore['friend2'] = 'jingxuan'
print(mycore['friend2'])
print('示例结束：向字典中添加元素')

# 一个 key 只能对应一个 value
# 避免 key 不存在的错误，通过 dict 提供的 get() 方法，如果 key 不存在，可以返回 None，或者自己指定的 value
print('示例开始：使用 get() 方法获取字典中的值')
xinxi = mycore.get('miao', '找不到')
print(xinxi)
print('示例结束：使用 get() 方法获取字典中的值')

# 2.13 集合（set）
# set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能重复，所以，在 set 中，没有重复的 key
print('示例开始：创建和查看集合')
set1 = {1, 2, 3}
set2 = set([1, 2, 3, 4])
print(f'{set1}and{set2}')
print('示例结束：创建和查看集合')

print('示例开始：向集合中添加元素')
# 通过 add(key) 方法可以添加元素到 set 中
set1.add(100)
print(set1)
print('示例结束：向集合中添加元素')

print('示例开始：从集合中删除元素')
# 通过 remove(key) 方法可以删除元素
set1.remove(1)
print(set1)
print('示例结束：从集合中删除元素')

'''
终端输出
示例开始：使用单引号和双引号输出字符串
hello world
hello world
示例结束：使用单引号和双引号输出字符串   
示例开始：使用 print() 函数输出多个字符串
hello world cheral chen
示例结束：使用 print() 函数输出多个字符串
示例开始：使用 print() 函数打印整数和计算结果
300
300
示例结束：使用 print() 函数打印整数和计算结果
示例开始：使用 input() 函数获取用户输入并输出
your wife叫什么？
your wife named
示例结束：使用 input() 函数获取用户输入并输出
示例开始：变量的定义和赋值
1
ABC
示例结束：变量的定义和赋值
示例开始：定义和使用常量
3.14159265359
示例结束：定义和使用常量
示例开始：使用 if 语句进行条件判断
haha,1>0
示例结束：使用 if 语句进行条件判断
示例开始：打印整数
100
示例结束：打印整数
示例开始：打印浮点数
9.9
示例结束：打印浮点数
示例开始：使用单引号和双引号输出字符串
hello
hello!
示例结束：使用单引号和双引号输出字符串
示例开始：字符串包含单引号时使用双引号括起来
hello'cheralchen'
示例结束：字符串包含单引号时使用双引号括起来
示例开始：使用转义字符和原始字符串
'这是单引号'"这是双引号"
'这是单引号'"这是双引号"
'这是单引号'
第一行
这是第二行:换行了
        制表
这是一个斜杠:\
\n换行无效
示例结束：使用转义字符和原始字符串
示例开始：使用三个单引号表示多行字符串
line1
line2
line3
line4
line5
line1\n
line2
line3
line4
line5
示例结束：使用三个单引号表示多行字符串
示例开始：使用 % 进行字符串格式化
I have 3 cats named miaomiao, hei, sanmiao
示例结束：使用 % 进行字符串格式化
示例开始：使用 f-string 进行字符串格式化
我老婆是cheralchen, 我有1个老婆
示例结束：使用 f-string 进行字符串格式化
示例开始：计算成绩提升率并进行字符串格式化
debug...去年成绩72,今年成绩85,提升率为18.1%
debug...去年成绩72,今年成绩85,18.1%
示例结束：计算成绩提升率并进行字符串格式化
示例开始：创建和查看列表
['cheralchen', 'ruikang']
示例结束：创建和查看列表
示例开始：获取列表元素个数
2
示例结束：获取列表元素个数
示例开始：使用索引访问列表元素
cheralchen
ruikang
示例结束：使用索引访问列表元素
示例开始：在列表末尾添加元素
['cheralchen', 'ruikang', 'bo']
示例结束：在列表末尾添加元素
示例开始：在指定位置插入元素
['cheralchen', 'jingxuan', 'ruikang', 'bo']
示例结束：在指定位置插入元素
示例开始：删除列表元素
['cheralchen', 'jingxuan', 'ruikang', 'bo', 'test1']
['cheralchen', 'jingxuan', 'ruikang', 'bo']
['test2', 'cheralchen', 'jingxuan', 'ruikang', 'bo']
['cheralchen', 'jingxuan', 'ruikang', 'bo']
示例结束：删除列表元素
示例开始：修改列表元素
['mywife', 'jingxuan', 'ruikang', 'bo']
示例结束：修改列表元素
示例开始：列表元素的数据类型可以不同
['Apple', 123, True]
['python', 'java', ['asp', 'php'], 'scheme']
4
php
示例结束：列表元素的数据类型可以不同
示例开始：创建空列表
[]
0
示例结束：创建空列表
示例开始：创建和查看元组
('cheralchen', 'ruikang')
cheralchen
示例结束：创建和查看元组
示例开始：创建空元组
()
示例结束：创建空元组
示例开始：创建只包含一个元素的元组
(1,)
示例结束：创建只包含一个元素的元组
示例开始：使用索引取出嵌套列表中的元素
Apple
Python
Bob
示例结束：使用索引取出嵌套列表中的元素
示例开始：使用 if-elif-else 进行年龄判断
kid, your age is 3
示例结束：使用 if-elif-else 进行年龄判断
示例开始：根据用户输入的出生年份进行判断
几几年出生:
已获取用户输入:, 正在调用'根据用户输入的出生年份进行判断'示例
调用'根据用户输入的出生年份进行判断'示例出现报错, 报错为invalid literal for int() with base 10: ''
示例结束：根据用户输入的出生年份进行判断
示例开始：简单的数学计算
6
示例结束：简单的数学计算
示例开始：使用 for...in 循环遍历列表
cheralchen
ruikang
示例结束：使用 for...in 循环遍历列表
示例开始：使用 for...in 循环计算 1 - 100 的整数之和
5050
示例结束：使用 for...in 循环计算 1 - 100 的整数之和
示例开始：使用 while 循环
x为9
示例结束：使用 while 循环
示例开始：使用 for...in 循环对列表中的每个名字打印出 Hello, xxx!
hello,Bart
hello,Lisa
hello,Adam
示例结束：使用 for...in 循环对列表中的每个名字打印出 Hello, xxx!
示例开始：使用 break 语句提前结束循环
105
示例结束：使用 break 语句提前结束循环
示例开始：使用 continue 语句跳过特定的循环
0
3
4
5
6
示例结束：使用 continue 语句跳过特定的循环
示例开始：创建和访问字典
cheralchen
示例结束：创建和访问字典
示例开始：向字典中添加元素
jingxuan
示例结束：向字典中添加元素
示例开始：使用 get() 方法获取字典中的值
找不到
示例结束：使用 get() 方法获取字典中的值
示例开始：创建和查看集合
{1, 2, 3}and{1, 2, 3, 4}
示例结束：创建和查看集合
示例开始：向集合中添加元素
{1, 2, 3, 100}
示例结束：向集合中添加元素
示例开始：从集合中删除元素
{2, 3, 100}
示例结束：从集合中删除元素
PS C:\Users\admin> 
'''

# 结束语
# 恭喜你！你已经完成了这个Python基础学习项目。现在你对Python的基础内容有了一定的了解。
# 接下来，多复制这些代码到文件里跑一跑，改改里面的值试试。记住，编程就是不断练习，错了也没关系。