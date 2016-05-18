from bs4 import BeautifulSoup
import requests
import urllib
import time

urls = ['http://www.yaojingweiba.com/manhua/fairytail484_{}.shtml'.format(str(i)) for i in range(0,30)]

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
          'Cookie':'__cfduid=dc023d7cf55e655e7788b652f8c801e051460446935; BAIDU_SSP_lcr=https://www.baidu.com/link?url=Sy4mT_BZ_Qd_Jr9TW_aZoDvoJV6h8rD9W2zr8Y5dWKP9wEP4eSbRnn7YDeCUbx2S&wd=&eqid=a6f1ae8b0008cf2100000003570cce8a; origin_num17919=3; CNZZDATA4306751=cnzz_eid%3D1173148498-1460445290-null%26ntime%3D1460456102; cscpvrich_fidx=3'}

url = 'http://www.yaojingweiba.com/manhua/fairytail484_00.shtml'

def get_img(url):
    source_code = requests.get(url, headers=header)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, 'lxml')

    download_links = []

    folder_path = 'F://PycharmBench/FairyTail/'

    for pic_tag in soup.find_all('img'):
        pic_links = pic_tag.get('src')
        download_links.append(pic_links)
        print(pic_links)

    print(download_links)

    for item in download_links:
        time.sleep(0.5)
        urllib.urlretrieve(item, folder_path + item[-7:])
        print('Done')

for url in urls:
    get_img(url)

'''
GET /uploads/manhua/481/03.png HTTP/1.1
Host: www.yaojingweiba.com
Connection: keep-alive
Cache-Control: max-age=0
Accept: image/webp,image/*,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36
Referer: http://www.yaojingweiba.com/manhua/fairytail481_3.shtml
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: __cfduid=dc023d7cf55e655e7788b652f8c801e051460446935; BAIDU_SSP_lcr=https://www.baidu.com/link?url=Sy4mT_BZ_Qd_Jr9TW_aZoDvoJV6h8rD9W2zr8Y5dWKP9wEP4eSbRnn7YDeCUbx2S&wd=&eqid=a6f1ae8b0008cf2100000003570cce8a; origin_num17919=3; CNZZDATA4306751=cnzz_eid%3D1173148498-1460445290-null%26ntime%3D1460456102; cscpvrich_fidx=3
If-None-Match: "c03ed3d9ec93d11:0"
If-Modified-Since: Mon, 11 Apr 2016 12:22:44 GMT
'''