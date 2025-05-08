import requests
import json
def f():
    apiname = '热搜'
    print(f'正在调用{apiname}...')
    hots = ['历史上的今天', '微信读书', 'HelloGitHub']
    hotsresult = []
    try:
        for hot in hots:
            result = requests.get(f'https://api.pearktrue.cn/api/dailyhot/?title={hot}').text
            hotsresult.append(result)
        print(f'{hotsresult}\n')
        return hotsresult
    except Exception as e:
        print(f'{apiname}出现错误, 错误信息: {e}')
f()
'''hots = ['哔哩哔哩', 'AcFun', '微博', '知乎', '知乎日报', '百度', 
'抖音', '豆瓣电影', '豆瓣讨论小组', '百度贴吧', '少数派', 'IT之家', 
'IT之家「喜加一」', '简书', '澎湃新闻', '今日头条', '36 氪', '51CTO', 
'CSDN', '稀土掘金', '腾讯新闻', '网易新闻', '吾爱破解', '全球主机交流', 
'虎嗅', '爱范儿', '英雄联盟', '原神', '崩坏3', '崩坏：星穹铁道', 
'微信读书', 'NGA', 'V2EX', 'HelloGitHub', '中央气象台', '中国地震台', 
'历史上的今天']'''