import re
import threading
import time
from urllib import response
from wsgiref import headers
import requests

# 访问一个网页
# def run():
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'

#     }
#     response = requests.get("https://www.linuxcool.com/", headers=headers)
#     print(response.text)


# if __name__ == "__main__":
#     run()

# 下载账号图片

# def run():
#     response = requests.get(
#         "http://img.cyol.com/img/edu/attachement/jpg/site2/20170811/IMG4524155117.jpg")

#     with open("img.jpg", "wb") as f:
#         f.write(response.content)
#         f.close


# if __name__ == "__main__":
#     run()


linuxcool_list_all = []  # list url
all_a_link_urls = []  # 图片列表页面的数组
g_lock = threading.Lock()  # 初始化一个锁

# 定义一个 spider 类


class spider():
    # 定义一个初始化的函数
    def __init__(self, linuxcool_url, headers):
        self.linuxcool_url = linuxcool_url
        self.headers = headers

# 定义一个 getUrls 函数
    def getUrls(self, start_page, page_num):
        global linuxcool_list_all

        for i in range(start_page, page_num+1):
            url = self.linuxcool_url % i
            linuxcool_list_all.append(url)


if __name__ == "__main__":
    # 定义一个请求头 字典类型
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
    }
    linuxcool_url = 'https://www.linuxcool.com/category/file/page/%d'  # 图片集和列表规则

    spider = spider(linuxcool_url, headers)
    spider.getUrls(1, 32)
    print(linuxcool_list_all)


class Producer(threading.Thread):
    def run(self):
        global linuxcool_list_all
        while len(linuxcool_list_all) > 0:
            g_lock.acquire()
            page_url = linuxcool_list_all.pop
            g_lock.release()
            try:
                print(page_url)
                response = requests.get(page_url, headers=headers, timeout=3)
                all_link = re.findall(
                    '<a rel=\"bookmark\" href="(.*?)"></a>', response.text, re.S)
                global all_a_link_urls
                g_lock.acquire()
                all_a_link_urls += all_link
                print(all_a_link_urls)
                g_lock.release()
                time.sleep(1)
            except:
                pass


for x in range(2):
    t = Producer()
    t.start()
