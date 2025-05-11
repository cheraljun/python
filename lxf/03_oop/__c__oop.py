class Animal:
    def __init__(self):
        pass
    def run(self):
        print('animal is running!')
        return 'animal is running!'
'''
在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
继承有什么好处？最大的好处是子类获得了父类的全部功能。
由于Animal实现了run()方法，因此，Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
'''

# 类
class Catsanmiao(Animal):
    def __init__(self):
        pass
# 实例化
sanmiao = Catsanmiao()
# 访问
sanmiao.run()

'''
当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的run()等函数。
'''
# 类
class Catmiaomiao(Animal):
    def __init__(self):
        pass
    def run(self):
        print('cat is running!')
        return 'cat is running!'
# 实例化
miaomiao = Catmiaomiao()
# 访问
miaomiao.run()