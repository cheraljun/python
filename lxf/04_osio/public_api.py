import requests
import os

'''
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache'), exist_ok=True)
cachepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache', 'cache.json')
'''

def dcrt(func):
    def wrapper(*args, **kwargs):
        print('start!')
        result = func(*args, **kwargs)
        print('end!')
        return result  
    return wrapper

@dcrt
def gold():
    while True:
        try:
            result = requests.get(url='https://api.pearktrue.cn/api/goldprice/').text
            print(result)
            return result
        except Exception as e:
                print(f'{e}\nretry?')
                continue
while True:
    gold()