mycore = {'wife': 'cheralchen', 'friend': 'ruikang'}
print(mycore['wife'])

mycore['friend2'] = 'jingxuan'
print(mycore['friend2'])

'''
一个key只能对应一个value
避免key不存在的错误
通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
'''
xinxi = mycore.get('miao', '404notfound')
print(xinxi)