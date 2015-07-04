# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:35:05 2015
@author: Moon
"""

import os, random, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

file_path = 'C:/1save/jpStock/rawPython/' #檔案路徑的代號，這邊放歷史資料
history_list = []
for name in os.listdir(file_path):
    history_list.append(name)

#可能要從這邊建立,比較符合python的語法
#把他寫成 def
"""
history_number = int(len(history_list)) - 1
string = {}
for i in range(0, 9):
  string['d' + str(i)] = history_list[history_number]
  history_number = history_number - 1
"""
"""
#下面這一行,是用來排序array 平常不需要用
b = OrderedDict(sorted(string.items()))
print (b) 
print (string[key])
"""


def sortDataFromNew (source_list, index):
    #source_list,是目標的list,第二個是存放目標的diction名字,第三個是裡面的code
    history_number = int(len(source_list)) - 1   
    code = str(index)
    def_diction = {}
    for i in range(history_number):
        def_diction[code + str(i)] = source_list[history_number]
        history_number = history_number - 1
    return def_diction

#d0 最新日期
string = sortDataFromNew (history_list, 'd')

"""
#測試 d0 到 d4 是不是會撈到歷史資料
for i in range(5):
    print (string['d'+ str(i)])
"""
csv_columns = ['code','market','name','industry','start','high','low','end','volumn','daily_money']
pre_array = pd.read_csv(file_path + string['d0'], encoding = 'utf-8')
#d0_array = pre_array.reindex(columns = csv_columns)
#
#d0_array = pd.DataFrame(pre_array, index = range(4000), columns = csv_columns)

pre_array.columns = csv_columns #把col 轉成英文

print (pre_array.columns) #到這裡成功了，接下來是把他拿進新的array
#print (pre_array.head(5)) #我只要code，名，始，高，安，終
#print (d0_array.index)

pre_array['volumn'] = pre_array['volumn'].astype(int) #先把vol換成int
pre_array = pre_array[pre_array.volumn != 0] #然後在array裡面去掉vol = 0
pre_array.index = pre_array['code'] #把index設定成code之後才好合併

d0_array = pre_array
print (d0_array.head(3))
del pre_array
print (pre_array)

#date_d0 = history_list[d0]  #這是為了給後面的csv檔有日期
#date_d1 = history_list[d1]
#print (date_d0)
#print (date_d1)

