'''
set和dict类似，也是一组key的集合，但不存储value。
由于key不能重复，所以，在set中，没有重复的key。
'''
gogo = {1, 2, 3}
lolo = set([1, 2, 3, 4])
print(f'{gogo}and{lolo}')

'''
通过add(key)方法可以添加元素到set中
'''
gogo.add(100)
print(gogo)

'''
通过remove(key)方法可以删除元素：
'''
gogo.remove(1)
print(gogo)