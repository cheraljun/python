n = 1 + 2 + 3
print(n)
'''
Python的循环有两种
一种是for...in循环
依次把list或tuple中的每个元素迭代出来
'''
friends = ['cheralchen', 'ruikang']
for friend in friends:
    print(friend)
'''
计算1-100的整数之和
'''
x = 0
for n in range(101):
    x = x + n
print(x)
'''
第二种循环是while循环，
只要条件满足，就不断循环，
条件不满足时退出循环。
'''
x = 9
while x == 9:
    print('x为9')
    break

'''
请利用循环依次对list中的每个名字打印出Hello, xxx!：
'''
L = ['Bart', 'Lisa', 'Adam']
for boy in L:
    print(f'hello,{boy}')
'''
break
break的作用是提前结束循环
'''
x = 0
for n in range(101):
    x = x + n
    if x >= 100:
        break
print(x)
'''
continue
continue语句，跳过当前的这次循环，直接开始下一次循环
'''
'''
打印0-6，不打印1和2
'''
for x in range(7):
    if x == 1 or x == 2:
        continue
    else:
        print(x)
