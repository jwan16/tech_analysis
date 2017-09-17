
import pymongo
import pandas
import bs4 as bs
import urllib.request
import re
from socket import error as SocketError
import errno
import pandas as pd
import requests
from datetime import datetime

period1 = 319579200
period2 = 1505145600
def get_historical_price(stock_id, start_date, end_date):
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
        'Connection': 'Keep-Alive',
        'Content-Type': 'text/plain; Charset=UTF-8',
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'Cookie': 'B=4aos411brv8q6&b=3&s=a7; PRF=t%3D0' + str(stock_id) + '.HK; bnpt=1501232783&pnid=&pnct=',
    }
    period1 = datetime.strptime(start_date, '%Y-%m-%d').strftime('%s')
    period2 = datetime.strptime(end_date, '%Y-%m-%d').strftime('%s')
    url = 'https://query1.finance.yahoo.com/v7/finance/download/' + stock_id + '.HK?period1=' + str(period1) + '&period2=' + str(period2) + '&interval=1d&events=history&crumb=tgIGmTK3EA.'
    data = requests.get((url),headers=headers).text
    price_list = []
    data2 = data.split('\n')
    print(data2)
    for a in data2:
        price_list.append(a.split(','))
    return price_list
print(get_historical_price('0151', '2015-01-01', '2015-01-20'))
