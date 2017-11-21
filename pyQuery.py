# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:29:26 2017

@author: ADMIN
"""

from pyquery import PyQuery as pq
#from tkinter import filedialog
import codecs
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
deal_period = ""
deal_price = ""
deal_volume = ""
deal_value = ""

#ul_listContent = ''''''
#selected_file_name = filedialog.askopenfilename()
#ul = pq(ul_listContent)
#ul = pq(filename=selected_file_name)
#li_list = ul('li')

output_file = codecs.open(output_file_name,"a", "utf-8")

url = 'https://bj.lianjia.com/chengjiao/pg16c1111027380129/'
html = requests.get(url).content.decode('utf-8')
tree = etree.HTML(html)
li_list = tree.xpath(".//ul[@class='listContent']/li")

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

            totalPrice = pq(address).children().eq(2)
            number = totalPrice.children().eq(0)
            #print(number)
            deal_price = number.text()

        flood_list = pq(info).children().eq(2)
        for flood in flood_list:
            positionInfo = pq(flood).children().eq(0)
            #print(positionInfo)
            deal_positionInfo = positionInfo.text()

            source = pq(flood).children().eq(1)
            #print(source)
            deal_source = source.text()

            unitPrice = pq(flood).children().eq(2)
            number = unitPrice.children().eq(0)
            #print(number)
            deal_value = number.text()

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

            askValue = dealCycleTxt.children().eq(0)
            #print(askValue)
            deal_ask = askValue.text()

            dealPeriod = dealCycleTxt.children().eq(1)
            #print(dealPeriod)
            deal_period = dealPeriod.text()

        if (deal_source == deal_source_lianjia):
            result = deal_date  + "\t" + deal_title + "\t" + deal_houseInfo + "\t" + deal_positionInfo + "\t" + deal_locationInfo + "\t" + deal_source + "\t" +  deal_ask  + "\t" + deal_period + "\t" + deal_price + "\t" + deal_value
            print(result)
            output_file.write(result)
            output_file.write("\n")

output_file.close()