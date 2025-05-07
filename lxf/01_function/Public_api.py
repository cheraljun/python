import requests
import time
def loveword():
    apiname = '情话api接口'
    print(f'正在调用{apiname}...')
    lovelist = []
    count = 0
    try:
        for i in range(1, 101, 1):
            result = requests.get(url='https://api.pearktrue.cn/api/jdyl/qinghua.php', timeout=300).text
            if result:
                count = count + 1
                print(f'{apiname}第{count}次调用成功!{result}')
                lovelist.append(result)
        return lovelist
    except Exception as e:
        print(f'{apiname}出现错误, 错误信息: {e}')

lovewords = loveword()
print(lovewords)