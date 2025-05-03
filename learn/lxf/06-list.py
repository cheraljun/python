列表
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

查看列表
friends = ['cheralchen', 'ruikang']
print(friends)

列表元素个数
print(len(friends))

索引
print(friends[0])
print(friends[1])

添加元素
friends.append('bo')
print(friends)

添加到指定位置
friends.insert(1, 'jingxuan')
print(friends)

删除
删除末尾
friends.append('test1')
print(friends)
friends.pop()
print(friends)
#删除指定位置
friends.insert(0, 'test2')
print(friends)
friends.pop(0)
print(friends)

变更
friends[0] = 'mywife'
print(friends)

list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
print(L)
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(len(s))
拿到'php'
print(s[2][1])

空列表
L = []
print(L)
print(len(L))