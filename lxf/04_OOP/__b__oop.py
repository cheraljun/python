# 类
class Car:
    def __init__(self, color = None, drive = None, passenger = None, *args, **kwargs):
        self.__color = color
        self.drive = drive
        self.passenger = passenger
        self.args = args
        self.kwargs = kwargs
    def start(self):
        return f'haha! the {self.drive} power {self.__color} car is started with {self.passenger} passenger!'
    def getcolor(self):
        return self.__color
    
# 实例化 实例化（创建对象）是独立于 “访问” 的操作
mycar = Car('yellow', 'electronic', 2)

# 访问 发生在实例化之后，包括对属性（公有 / 私有）的读写和对方法的调用。
d = mycar.drive
p = mycar.passenger
try:
    c = mycar.color
except Exception as e:
    print(e)
finally:
    c = '未获取'
print(f'{d}, {p}, {c}')

r = mycar.start()
print(r)

r = mycar.getcolor()
print(r)

print(dir(Car))