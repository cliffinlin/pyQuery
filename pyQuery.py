# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:29:26 2017

@author: ADMIN
"""

from pyquery import PyQuery as pq
#from tkinter import filedialog
import codecs
import os
import re
import requests
from lxml import etree

deal_source_lianjia = '链家成交'
output_file_name = "listContent.txt"

deal_title = ""
deal_houseInfo = ""
deal_positionInfo = ""
deal_locationInfo = ""
deal_source = ""
deal_date = ""
deal_ask = ""
deal_ask_text = ""
deal_delt = ""
deal_period = ""
deal_value = ""
deal_volume = ""
deal_price = ""

#ul_listContent = ''''''
#selected_file_name = filedialog.askopenfilename()
#ul = pq(ul_listContent)
#ul = pq(filename=selected_file_name)
#li_list = ul('li')

if os.path.exists(output_file_name):
    os.remove(output_file_name)

output_file = codecs.open(output_file_name,"a", "utf-8")

url_base = "https://bj.lianjia.com/chengjiao/"
region = "zaojunmiao"
sub_region_id = "c1111027380750"
pages = range(4)

for i in pages:
    #url = url_base + region + '"/' + "pg" + str(i+1)
    url = url_base + "pg" + str(i+1) + sub_region_id

    html = requests.get(url).content.decode('utf-8')
    tree = etree.HTML(html)
    li_list = tree.xpath(".//ul[@class='listContent']/li")

    #print(url)
    #output_file.write(url)
    #output_file.write("\n")

    for li in li_list:
        info_list = pq(li).children().eq(1)

        for info in info_list:
            title_list = pq(info).children().eq(0)
            for title in title_list:
                #print(pq(title))
                deal_title = pq(title).text()

            address_list = pq(info).children().eq(1)
            for address in address_list:
                houseInfo = pq(address).children().eq(0)
                #print(houseInfo)
                deal_houseInfo = houseInfo.text()

                dealDate = pq(address).children().eq(1)
                #print(dealDate)
                deal_date = dealDate.text()

                dealValue = pq(address).children().eq(2)
                number = dealValue.children().eq(0)
                #print(number)
                deal_value = number.text()

            flood_list = pq(info).children().eq(2)
            for flood in flood_list:
                positionInfo = pq(flood).children().eq(0)
                #print(positionInfo)
                deal_positionInfo = positionInfo.text()

                source = pq(flood).children().eq(1)
                #print(source)
                deal_source = source.text()

                dealPrice = pq(flood).children().eq(2)
                number = dealPrice.children().eq(0)
                #print(number)
                deal_price = number.text()

            dealHouseInfo_list = pq(info).children().eq(3)
            for dealHouseInfo in dealHouseInfo_list:
                dealHouseIcon = pq(dealHouseInfo).children().eq(0)

                dealHouseTxt = pq(dealHouseInfo).children().eq(1)
                #print(dealHouseTxt)
                deal_locationInfo = dealHouseTxt.text()

            dealCycleeInfo_list = pq(info).children().eq(4)
            for dealCycleeInfo in dealCycleeInfo_list:
                dealCycleIcon = pq(dealCycleeInfo).children().eq(0)

                dealCycleTxt = pq(dealCycleeInfo).children().eq(1)

                dealAsk = dealCycleTxt.children().eq(0)
                #print(askValue)
                deal_ask_text = dealAsk.text()
                deal_ask = re.findall("\d+",deal_ask_text)[0]

                dealPeriod = dealCycleTxt.children().eq(1)
                #print(dealPeriod)
                deal_period = dealPeriod.text()

            if (deal_source == deal_source_lianjia):
                result = deal_date  + "\t" + deal_title + "\t" + deal_houseInfo + "\t" + deal_positionInfo + "\t" + deal_locationInfo + "\t" + deal_source + "\t" +  deal_ask_text  + "\t" + deal_period + "\t"\
                         + deal_value + "\t" + deal_price + "\t"\
                         + deal_ask

                print(result)
                output_file.write(result)
                output_file.write("\n")

output_file.close()