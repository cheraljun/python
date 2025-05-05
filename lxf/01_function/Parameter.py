'''
参数
input output
定义函数的时候, 
我们把参数的名字和位置确定下来, 
函数的接口定义就完成了。
对于函数的调用者来说, 
只需要知道如何传递正确的参数, 
以及函数将返回什么样的值就够了

位置参数
就像经典奶昔的固定配方, 
数量和顺序都是确定的, 
调用函数时必须按照顺序传入对应数量的参数值。

位置参数样例：
make_strawberry_banana_smoothie 函数
定义了三个位置参数 strawberries、bananas 和 milk。
调用函数 make_strawberry_banana_smoothie(2, 1, 200) 时, 
传入的参数值 2、1、200 
会按照位置
依次赋值给 strawberries、bananas、milk, 
就像按照配方依次添加原料一样。
如果调用时参数数量不对, 
比如 make_strawberry_banana_smoothie(2, 1), 
Python 会报错, 因为它发现你没有按照配方准备好所有原料。
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

# 而对于n不等于64的其他情况, 就必须明确地传入n
result = power2(2, 3)
print(result)

'''
也可以不按顺序提供部分默认参数。
当不按顺序提供部分默认参数时, 需要把参数名写上。
非默认参数必须在默认参数之前。
'''
result = power2(2, n = 4)
print(result)

'''
可变参数
如同特色自由搭配奶昔, 
在基础原料的基础上, 允许顾客自由添加额外的水果, 
添加的数量和种类都不固定。
在函数里, 可变参数会把传入的额外参数打包成一个元组来处理。

make_custom_smoothie 函数有三个位置参数
 strawberries、bananas、milk, 
还有一个可变参数 *extra_fruits。
当调用 make_custom_smoothie(2, 1, 200, "3 颗蓝莓", "1 片芒果") 时, 
2、1、200 分别对应位置参数, 
而 "3 颗蓝莓" 和 "1 片芒果" 会被打包成一个元组, 
赋值给 extra_fruits。
若调用 make_custom_smoothie(2, 1, 200), 没有传入额外水果, 
那么 extra_fruits 就是一个空元组。
也就是说, 顾客可以选择不添加额外水果, 只用基础原料制作奶昔。
定义一个名为 make_custom_smoothie 的函数, 用于制作特色自由搭配奶昔
该函数接收三个位置参数 strawberries（草莓数量）、bananas（香蕉数量）、milk（牛奶毫升数）
以及一个可变参数 *extra_fruits, 用于接收顾客额外添加的水果信息
'''

'''
制作一杯添加额外水果的奶昔函数
'''
def make_custom_smoothie(strawberries, bananas, milk, *extra_fruits):
    '''
    创建一个字符串 fruit_info, 用于存储制作奶昔所使用的基础原料信息
    这里使用 f 字符串将传入的 strawberries、bananas 和 milk 的值格式化到字符串中
    '''
    fruit_info = f"{strawberries} 颗草莓、{bananas} 根香蕉和 {milk} 毫升牛奶"
    '''
    使用 if 语句检查可变参数 extra_fruits 是否包含元素
    如果 extra_fruits 不为空元组, 说明顾客添加了额外的水果
    '''
    if extra_fruits:
        '''
        使用字符串的 join 方法将 extra_fruits 元组中的元素用逗号连接成一个字符串
        存储在 extra_fruit_str 变量中
        将额外水果的信息添加到基础原料信息后面
        形成包含所有原料信息的新字符串
        '''
        extra_fruit_str = ", ".join(extra_fruits)
        fruit_info = fruit_info + ", 额外添加了 " + extra_fruit_str
    '''
    使用 print 函数输出最终的原料信息, 表明用这些原料制作了一杯特色自由搭配奶昔
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