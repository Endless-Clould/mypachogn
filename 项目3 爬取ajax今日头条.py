import requests
from urllib.parse import urlencode
from retry import retry
import os
from hashlib import md5
from multiprocessing import Pool

headers = {
    "accept": "application/json, text/javascript",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "UM_distinctid=1683d0a591db9-0fe80248372b1d-3c604504-100200-1683d0a591e114; csrftoken=1d0586596d0ff8088cb4aeea1a3bf4ca; tt_webid=6687905148181120525; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6687905148181120525; CNZZDATA1259612802=2101811796-1547210491-%7C1557148926; __tasessionId=9h12xnkn31557149269308; s_v_web_id=1f0380d970060a70567ad7c0fb1e8dd2",
    "referer": "https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}


def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'

    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


# @retry()
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            print(title)
            try:
                images = item.get('image_list')
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }
            except:
                print('这是空的..可惜')

                # yield {
                #     'image':image.get('url'),
                #     'title':title
                # }


# for i in range(12):
#     i=i*20
#     x = get_page(i)
#     # print(x)
#     get_images(x)
import time

i = 0


def save_image(item):
    global i

    if not os.path.exists(item.get('title')):

        try:
            os.mkdir(item.get('title'))

        except:
            print('没有title,跳过>>>>>>>')
    try:
        response = requests.get(item.get('image'))
        file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else:
            print('download', file_path)
    except:
        print('no')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(1, 20 + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
    print('爬取完毕')
