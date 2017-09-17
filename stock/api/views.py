# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import django_tables2 as tables

import pymongo
from datetime import datetime
client = pymongo.MongoClient('mongodb://13.76.163.216')
db = client['stock']
his_price = db['historical_price']
stock_list = his_price.distinct('id')
# Create your views here.

class NameTable(tables.Table):
    id = tables.Column()
    open = tables.Column()
    adj_close = tables.Column()
    close = tables.Column()
    volume = tables.Column()
    high = tables.Column()
    low = tables.Column()
    date = tables.Column()

def IndexView(request):
    stock_list = his_price.find({'id':'0151'}, {'_id':False})

    table = NameTable(stock_list)
    table.paginate(page=request.GET.get('page', 1), per_page=25)
    context = {
        "stock_list": stock_list,
        "table": table
    }
    return render(request, "api/index.html", context)