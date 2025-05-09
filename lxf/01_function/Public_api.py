import requests

def log(func):
    def wrapper(*args, **kwargs):
        apiname = ''
        print(f'正在调用{apiname}api...正在启动{func.__name__}函数!')
        result = func(*args, **kwargs)
        print(f'{apiname}api调用成功!{func.__name__}函数正常执行!')
        return result
    return wrapper

@log
def gold():
    try:
        result = requests.get('https://api.pearktrue.cn/api/goldprice/').text
        print(result)
        return result
    except Exception as e:
        print(f'出现错误, 错误信息: {e}')
gold()