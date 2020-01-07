import time
import unittest
import requests
from lxml import html
import os


'''
哈哈，抓的是缩略图，以后再改了
'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_scrape(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/79.0.3945.88 Safari/537.36 '
        }
        page = requests.get('https://movie.douban.com/subject/3742360/all_photos',
                            headers=headers)
        tree = html.fromstring(page.content)
        nodes = tree.xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/ul/li[*]/a/img/@src')
        folder = tree.xpath('//*[@id="content"]/h1/text()')[0]
        dir_path = './data/' + folder;
        print(dir_path)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        print(type(nodes))
        for url in nodes:
            time.sleep(1)
            print(url)
            file_path = dir_path + '/' + str(url).split('/')[-1]
            with open(file_path, 'wb+') as f:
                response = requests.get(url, headers=headers)
                f.write(response.content)


if __name__ == '__main__':
    unittest.main()
