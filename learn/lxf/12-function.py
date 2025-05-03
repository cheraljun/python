import sys
sys.path.append('C:\\Users\\admin\\Desktop\\cheralpython\\play\\siliconflow\\robot')
from robot_function import robot

'''
定义函数
在Python中，定义一个函数要使用def语句，
依次写出函数名、括号、括号中的参数和冒号:
然后，在缩进块中编写函数体，
函数的返回值用return语句返回。
'''

'''
求绝对值函数
'''
def jueduizhi(x): # def, 函数名, 参数
    if x >= 0:
        return x # return
        print(x)
    else:
        return -x
        print(-x)
'''
调用函数
'''
result = jueduizhi(66)
print(result)

'''
mywife function
'''
def mywife():
    cheral = 'cheralchen'
    return f'''My wife {cheral}
I love my wife {cheral}
My wife {cheral} very very beautiful'''

'''
调用函数
'''
result = mywife()
print(result)

'''
空函数
'''
def nothing():
    pass

'''
返回多个值
返回3个偶数
'''
def oushu(x, y ,z):
    x = x * 2
    y = y * 2
    z = z * 2
    return(x, y, z)
'''
Python的函数返回多值其实就是返回一个tuple
'''
result = oushu(8, 8, 8)
print(result)

'''
练习
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 
ax²+bx+c=0的两个解。
求根公式x=(-b±√(b²-4ac))/2a
'''
import math
def quadratic(a, b ,c):
    pan = b ** 2 - 4 * a * c
    if pan < 0:
        return '方程{a}x²+{b}x+{c}=0无实数解'
    else:
        x1 = ((-b + math.sqrt(pan))) / 2 * a
        x2 = ((-b - math.sqrt(pan))) / 2 * a
        return (x1, x2)

result = quadratic(60, -600, 6)
print(result)

'''
谬误样例
在这个函数中，return print(...) 会让函数返回 None，
因为 print 函数返回的就是 None。
所以，变量 result 得到的值是 None，而非方程的解。
'''
import math
def quadratic(a, b ,c):
    x1 = ((-b + math.sqrt(b ** 2 - 4 * a * c))) / 2 * a
    x2 = ((-b - math.sqrt(b ** 2 - 4 * a * c))) / 2 * a
    return print(f'方程{a}x²+{b}x+{c}=0的两个解是{x1}和{x2}')

result = quadratic(1, 2, 1)
print(result)
'''
输出为：
方程1x²+2x+1=0的两个解是-1.0和-1.0
None

第一行显示了方程的两个解，
这是因为函数里的 print 语句把结果输出到了终端。
而第二行的 None 是由于 return 语句后面跟着 print 函数调用，
print 函数返回 None，所以函数返回的也是 None，
这就导致 result 变量的值为 None，进而在打印 result 时输出了 None。
'''

'''
参数
input output
定义函数的时候，
我们把参数的名字和位置确定下来，
函数的接口定义就完成了。
对于函数的调用者来说，
只需要知道如何传递正确的参数，
以及函数将返回什么样的值就够了
'''

'''
位置参数
就像经典奶昔的固定配方，
数量和顺序都是确定的，
调用函数时必须按照顺序传入对应数量的参数值。
'''

'''
位置参数样例：
make_strawberry_banana_smoothie 函数
定义了三个位置参数 strawberries、bananas 和 milk。
调用函数 make_strawberry_banana_smoothie(2, 1, 200) 时，
传入的参数值 2、1、200 
会按照位置
依次赋值给 strawberries、bananas、milk，
就像按照配方依次添加原料一样。
如果调用时参数数量不对，
比如 make_strawberry_banana_smoothie(2, 1)，
Python 会报错，因为它发现你没有按照配方准备好所有原料。
'''
def make_strawberry_banana_smoothie(strawberries, bananas, milk):
    print(f"我用 {strawberries} 颗草莓、{bananas} 根香蕉和 {milk} 毫升牛奶制作了一杯草莓香蕉奶昔。")

'''按照配方制作奶昔'''
make_strawberry_banana_smoothie(2, 1, 200)


'''
默认参数
定义默认参数要牢记一点：默认参数必须指向不变对象！
'''
def power2(x, n = 64):
    value = x ** n
    return value

result = power2(2, )
print(result)

'''而对于n不等于64的其他情况，就必须明确地传入n'''
result = power2(2, 3)
print(result)
'''
也可以不按顺序提供部分默认参数。
当不按顺序提供部分默认参数时，需要把参数名写上。
非默认参数必须在默认参数之前。
'''
result = power2(2, n = 4)
print(result)

'''
可变参数
如同特色自由搭配奶昔，
在基础原料的基础上，允许顾客自由添加额外的水果，
添加的数量和种类都不固定。
在函数里，可变参数会把传入的额外参数打包成一个元组来处理。
'''

'''
make_custom_smoothie 函数有三个位置参数
 strawberries、bananas、milk，
还有一个可变参数 *extra_fruits。
当调用 make_custom_smoothie(2, 1, 200, "3 颗蓝莓", "1 片芒果") 时，
2、1、200 分别对应位置参数，
而 "3 颗蓝莓" 和 "1 片芒果" 会被打包成一个元组，
赋值给 extra_fruits。
若调用 make_custom_smoothie(2, 1, 200)，没有传入额外水果，
那么 extra_fruits 就是一个空元组。
也就是说，顾客可以选择不添加额外水果，只用基础原料制作奶昔。
定义一个名为 make_custom_smoothie 的函数，用于制作特色自由搭配奶昔
该函数接收三个位置参数 strawberries（草莓数量）、bananas（香蕉数量）、milk（牛奶毫升数）
以及一个可变参数 *extra_fruits，用于接收顾客额外添加的水果信息
'''

'''
制作一杯添加额外水果的奶昔函数
'''
def make_custom_smoothie(strawberries, bananas, milk, *extra_fruits):
    '''
    创建一个字符串 fruit_info，用于存储制作奶昔所使用的基础原料信息
    这里使用 f 字符串将传入的 strawberries、bananas 和 milk 的值格式化到字符串中
    '''
    fruit_info = f"{strawberries} 颗草莓、{bananas} 根香蕉和 {milk} 毫升牛奶"
    '''
    使用 if 语句检查可变参数 extra_fruits 是否包含元素
    如果 extra_fruits 不为空元组，说明顾客添加了额外的水果
    '''
    if extra_fruits:
        '''
        使用字符串的 join 方法将 extra_fruits 元组中的元素用逗号连接成一个字符串
        存储在 extra_fruit_str 变量中
        将额外水果的信息添加到基础原料信息后面
        形成包含所有原料信息的新字符串
        '''
        extra_fruit_str = ", ".join(extra_fruits)
        fruit_info = fruit_info + "，额外添加了 " + extra_fruit_str
    '''
    使用 print 函数输出最终的原料信息，表明用这些原料制作了一杯特色自由搭配奶昔
    '''
    print(f"我用 {fruit_info} 制作了一杯特色自由搭配奶昔。")


'''制作一杯添加额外水果的奶昔'''
make_custom_smoothie(2, 1, 200, "3 颗蓝莓", "1 片芒果")
'''制作一杯不添加额外水果的奶昔'''
make_custom_smoothie(2, 1, 200)

'''
可变参数例子2
加法
'''
def addfunction(*addnum):
    print(f'''\n正在调用加法函数...
正在打印参数...
当前的参数为{addnum}''')
    return sum(addnum)

result = addfunction(1, 2, 3, 4)
print(f'函数输出为{result}')

