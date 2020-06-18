# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 汪逢生
# @FILE     : es.py
# @Time     : 2020/6/17 10:03
# @Software : PyCharm


from elasticsearch import Elasticsearch, RequestsHttpConnection
import time

def get_time():
    time_str =  time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    es = Elasticsearch(
        ['es-cn-st21p5hmc000ew4xh.public.elasticsearch.aliyuncs.com'],
        http_auth=('elastic', 'qwer123.'),
        port=9200,
        use_ssl=False
    )
    return es

def close_conn(es):
    pass

def get_predict():
    es = get_conn()
    action = { "query": {
    "match": {
      "predict": "1"
    }
    },
    "sort": [
        {
      "ds": {
        "order": "asc"
                }
            }
        ],
        "size": 2000000
    }

    res = es.search(index="emotion_val", body=action)
    return res

def get_emotion_val():
    es = get_conn()
    action = {
        "sort": [
            {
                "predict": {
                    "order": "asc"
                }
            }
        ],
        "size": 2000000
    }

    res = es.search(index="emotion_val", body=action)
    return res

def get_rawdata():
    es = get_conn()
    action = {
        "size": 2000000
    }
    res = es.search(index="raw_data", body=action)
    return res

def get_midrawdata():
    es = get_conn()
    action = {"query": {
        "match": {
            "predict": "0"
        }
    },
        "sort": [
            {
                "ds": {
                    "order": "asc"
                }
            }
        ],
        "size": 200000
    }

    res = es.search(index="emotion_val", body=action)
    return res

if __name__ == "__main__":
    get_midrawdata()

