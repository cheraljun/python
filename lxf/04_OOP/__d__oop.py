class Car:
    '''
    在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
    因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
    '''
    wheel = 4

    def __init__(self, color = None, drive = None, passenger = None, *args, **kwargs):
        # 实例属性
        self.__color = color
        self.drive = drive
        self.passenger = passenger
        self.args = args
        self.kwargs = kwargs
    def start(self):
        return f'haha! the {self.drive} power {self.__color} car is started with {self.passenger} passenger!'
    def getcolor(self):
        return self.__color

print(Car.wheel)