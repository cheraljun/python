import requests
import time
class Api():
    def __init__(self, baseurl, param = ''):
        self.baseurl = baseurl
        self.param = param

    def search(self):
        while True:
            try:
                print(f'{self.baseurl}{self.param}')
                result = requests.get(f'{self.baseurl}{self.param}').text
                if result:
                    print(result)
                    return result
            except Exception as e:
                    print(f'{e}\nretry?')
                    time.sleep(1)
                    continue

gold = Api('https://api.pearktrue.cn/api/goldprice/') # 获取最新的黄金价格以及各种黄金的详细信息
gold.search()

recipe = Api('https://api.pearktrue.cn/api/cookbook/?search=', '鸡蛋布丁') # 查询菜谱信息，包括简介，材料，做法
recipe.search()

baidumap = Api('https://api.pearktrue.cn/api/baidumap/?keyword=', '广州') # 通过地名检索相关地点显示基础信息
baidumap.search()

'''while True:
    try:
        resp = requests.get('https://api.pearktrue.cn/api/baidumap/?keyword=广州').text
        if resp:
            print(resp)
    except Exception as e:
        print(f'{e}')
        continue'''