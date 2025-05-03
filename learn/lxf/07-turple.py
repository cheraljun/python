元组
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
turplefriends = ('cheralchen', 'ruikang')
print(turplefriends)
print(turplefriends[0])
t1 = ()
print(t1)
只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t2 = (1, )
print(t2)

练习
请用索引取出下面list的指定元素：
fruit = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

打印Apple:
print(fruit[0][0])
打印Python:
print(fruit[1][1])
打印Bob:
print(fruit[2][2])