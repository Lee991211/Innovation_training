# !/usr/bin/env Python3
# @Author   : 汪逢生
# @FILE     : zhihu.py
# @Time     : 2020/6/7 15:57
# @Software : PyCharm
#coding=utf-8
import json
from urllib.parse import urlencode
import requests
import re
import codecs
import time
import csv


def timeStamp(timeNum):
    timeStamp = float(timeNum)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return  otherStyleTime


class zhihuCrawler():
    def __init__(self,query):
        self.query = query
        f1 = open("../data/zhihu/"+str(query)+'answer.csv', 'w', encoding='utf-8',newline='')
        self.csv_writer1 = csv.writer(f1)
        self.csv_writer1.writerow(["question_name", "answer_content", "voteup_count",'comment_count','created_time','updated_time'])
        f2 = open("../data/zhihu/"+str(query)+'question.csv', 'w', encoding='utf-8',newline='')
        self.csv_writer2 = csv.writer(f2)
        self.csv_writer2.writerow(["question", 'description', 'follower_count', 'comment_count', 'answer_count', 'visits_count', 'updated_time'])

    def handle_url(self,url):
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'accept-encoding': 'gzip',
        'accept-language': 'en-GB,en;q=0.9,zh;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6,ja;q=0.5',
        "cache-control": "max-age=0",
        'cookie': '_xsrf=a21de17a-59ee-4d29-b4b9-5c397d0917ca; _zap=cce7d96b-ecd2-4953-b958-cc0bfbe9a2e7; BAIDU_SSP_lcr=https://www.google.com/; cap_id="NGM1OGZlYTgwMWU2NGI5YjgyZGQyYzJlYTIwZDYyMTc=|1587130242|8f2a774418c56fabb1f42aaf30d7e37dbd0df1a7"; capsion_ticket="2|1:0|10:1589482049|14:capsion_ticket|44:OGEzY2NkZGVjZTIzNDg2MGE1NWNkOTYwMTgxYWUzZWI=|0e51411a2863f1881abc1a57c7b1867e6b0a059464fa43e6a2e55bf97c86bc7d"; d_c0="ADCb102P-hCPTr5IshFBfxUARc-mRhjx2iY=|1584472689"; l_cap_id="MTI2ZDg3OWUxNmMwNDk2Y2ExYWI4ZjY5MDRjMGIyODQ=|1587130242|6c9a2dafefd22d23c9f19142a7fb4061ebc0f45f"; q_c1=e14ff8f74d144c4d9b4ce781405d22ca|1589200919000|1589200919000; r_cap_id="OGIzMzU4ZmVjODFhNDZkYzg3MWZhOTdhMDliYTExNDY=|1587130242|5e08cedf3450929c6b9816ca0dfef46c1248fa24"; tst=r; z_c0="2|1:0|10:1589482084|4:z_c0|92:Mi4xQWw0MEd3QUFBQUFBTUp2WFRZXzZFQ1lBQUFCZ0FsVk5aT0NxWHdDWEVhWUJXSE1BUzZuYnV6NURCSmNrNFlPNk9R|d2595436ce2f97f37b61de7c533b0415fd03bd8dc5b95c3d3199f7ab90bb5eeb"; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1589487035|1589486377',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
        response = requests.get(url, headers=headers)
        response.encoding='utf-8'
        pattern = re.compile(r'\\u003c/?em\\u003e')
        clear_text = pattern.sub("", response.text)
        result = json.dumps(response.json(), ensure_ascii=False)
        json_dict = json.loads(clear_text)
        for i in json_dict['data']:
            object = i['object']
            if object['type'] =='answer':
                question = object['question']['name']
                voteup_count =object['voteup_count']
                comment_count  =object['comment_count']
                created_time=timeStamp(object['created_time'])
                updated_time=timeStamp(object['updated_time'])
                content = object['content']
                content = re.sub(r'<[^>]+>', '', content)
                self.csv_writer1.writerow([question,content,voteup_count,comment_count,created_time,updated_time])
            elif object['type'] == 'question':
                question = object['title']
                description = object['description']
                follower_count = object['follower_count']
                comment_count = object['comment_count']
                answer_count = object['answer_count']
                visits_count= object['visits_count']
                updated_time = timeStamp(object['updated_time'])
                self.csv_writer2.writerow([question, description, follower_count, comment_count, answer_count, visits_count,updated_time])
        return clear_text

    def make_url(self,searchid, lcid, offset):
        baseurl = "https://api.zhihu.com/search_v3?advert_count=0&correction=1&"

        param = {
        "lc_idx": lcid,
        "limit": 20,
        "offset": offset,
        "q": self.query,
        "search_hash_id": searchid,
        "show_all_topics": 0,
        "t": "general",
        "time_zone": "three_months",
        'vertical_info': '0,0,0,0,0,0,0,0,0,0',
        }
        url = baseurl + urlencode(param)
        return url

    def main(self):
        # for
        lcid =27
        offset = 20
        search_id = 'e3ec8bd2f9ceb4097d18296511fbce33'
        for i in range(10):
            url = self.make_url(search_id, lcid, offset*i)
            self.handle_url(url)

if __name__ == '__main__':
    query='特朗普'
    zhihu = zhihuCrawler(query)
    url= zhihu.main()