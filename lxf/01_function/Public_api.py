import requests
class Api():
    def __init__(self, baseurl, param = ''):
        self.baseurl = baseurl
        self.param = param

    def search(self):
        while True:
            try:
                result = requests.get(f'{self.baseurl}{self.param}').text
                if result:
                    print(result)
                    return result
            except Exception as e:
                    print(f'{e}\nretry?')
                    continue

gold = Api('https://api.pearktrue.cn/api/goldprice/') # 获取最新的黄金价格以及各种黄金的详细信息
earthquake = Api('https://api.pearktrue.cn/api/earthquake/') # 查询全球范围内的地址响应震级，时间，经纬度，深度，位置信息
randompeople = Api('https://api.pearktrue.cn/api/random/people.php') # 随机返回一段长达48条信息的账号信息
dogword = Api('https://api.pearktrue.cn/api/jdyl/tiangou.php') # 随机返回一篇舔狗日记
recipe = Api('https://api.pearktrue.cn/api/cookbook/?search=', '鸡蛋布丁') # 查询菜谱信息，包括简介，材料，做法
baidumap = Api('https://api.pearktrue.cn/api/baidumap/?keyword=', '广州') # 通过地名检索相关地点显示基础信息

gold.search()
earthquake.search()
randompeople.search()
dogword.search()
recipe.search()
baidumap.search()