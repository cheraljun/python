条件判断
用if语句实现
如果if判断是False，不要执行if的内容，去把else执行了
注意不要少写了冒号:
elif是else if的缩写，完全可以有多个elif
age = 3
if age >= 18:
    print(f'adult, your age is {age}')
elif age >= 6:
    print(f'teenager, your age is {age}')
else:
    print(f'kid, your age is {age}')

再议input
这是因为input()返回的数据类型是str，str不能直接和整数比较，
必须先把str转换成整数。
Python提供了int()函数来完成这件事情
birth = input('几几年出生: ')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')