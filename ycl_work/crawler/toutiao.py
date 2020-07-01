# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 汪逢生


import json
from urllib.parse import urlencode
import requests
import time
import datetime




class toutiaocrawler():
    def __init__(self):
        '''
        cookie is not alway available,you must chang sometimes.
        '''
        self.cookie ='WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=fa5d065bb693c2003f5aaf0085d26081; SLARDAR_WEB_ID=45e67be6-0d81-45b5-8998-668f68051c53; ttcid=608b0e222f134da5bcac16b4bb4dda5f32; tt_webid=6835073330430019086; s_v_web_id=verify_kb334las_nfUlj2vd_g9cO_4ATb_BYuW_zQFyThA9c6hn; __tasessionId=hb6jn63b81591414540156; tt_webid=6835073330430019086; tt_scid=Bf71bLp3r.tDl7yku74LgVYAN8x0BoA32OxnUKp4Sn0R4CE8DJ-aA3eRlTjXU6P908d7'
        self.headers = {
            'cookie': self.cookie,
            'referer': 'https://www.toutiao.com/search/?keyword=%E6%96%B0%E5%86%A0%E7%96%AB%E6%83%85',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
        self.comment_headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
        self.offset=0

    def get_json(self,query,times):
        url = 'https://www.toutiao.com/api/search/content/?'
        query = query
        data = {
        'aid' : '24',
        'app_name' : 'web_search',
        'offset':times*20,
        'format':'json',
        'keyword': query,
        'autoload':'true',
        'count':'20',
        'en_qc':'1',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis',
        'timestamp':'1591334689562',
        '_signature':'eogINAAgEBC837G5qXUW1nqJSSAACRUUacJVWMYPAnDzgyhUN8Z50mnnocKxzlDN68ESVavW7QohTkc-zAqL6T3-Yix63Z7STBVenpHHWa-svVRQHbXc9VElqbkshKKcmNI'}
        data = urlencode(data)
        url = url + data
        return url


    def get_comment(self,url,number):
        common = []
        id = None
        if number==1:
            id = url.split('/')[4]
        if number==2:
            id = url
        url = self.get_comment_json(id)
        response = requests.get(url, headers=self.comment_headers)
        response.encoding = 'utf-8'
        html = response.content
        json_dict = json.loads(html.decode('utf-8'))
        for i in  json_dict['data']:
            common.append(i['comment']['text'])
        return common

    def get_comment_json(self,id):
        url = 'https://www.toutiao.com/article/v2/tab_comments/?'
        'aid=24&app_name=toutiao-web&group_id=6832123300156539399&item_id=6832123300156539399&offset=0&count=5'
        id = id
        data = {
            'aid': '24',
            'app_name': 'toutiao-web',
            'group_id':id,
            'item_id':id,
            'offset': '0',
            'count':'5'}
        data = urlencode(data)
        url = url + data
        return url
    def set_cookie(self,cookie):
        self.cookie=cookie

    def main(self,query):
        z_test = 0
        f = open('../data/toutiao/'+str(query)+'.txt', 'w+',encoding="utf-8")
        while True:
            z_test+=1
            url = self.get_json(query,self.offset)
            self.offset += 1
            summary_list = []
            response = requests.get(url, headers=self.headers)
            response.encoding = 'utf-8'
            html = response.content
            json_dict = json.loads(html.decode('utf-8'))
            # print(json_dict['count'])
            if json_dict['count']==0:
                if z_test==0:
                    print("cookie已过期，添加新cookie")
                print('finish crawling data')
                break
            for i in json_dict['data']:
                try:
                    mid = i['title'].replace('<em>', '').replace('</em>', '')
                    times = i['datetime']
                    try:
                        comment_url = i['display']['info']['url']
                        comment_list_=self.get_comment(comment_url,1)
                    except:
                        comment_url=i['id']
                        comment_list_ = self.get_comment(comment_url, 2)
                    f.write(str(mid) + ',' + str(times) + ',' + str(comment_list_)+'\n')
                except KeyError:
                    pass
            time.sleep(5)
        f.close()

if __name__ == '__main__':
    query = input('请输入想要查询的东西')
    # query = '特朗普'
    toutiaocrawler = toutiaocrawler()
    # cookie = input('请输入cookie')
    # toutiaocrawler.set_cookie(cookie)
    toutiaocrawler.main(query)