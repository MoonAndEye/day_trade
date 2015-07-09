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
# string['d0'] 表示最新的資料
# string['d1'] 表示前1天的資料
# string['d2'] 表示前2天的資料
"""
#測試 d0 到 d4 是不是會撈到歷史資料
for i in range(5):
    print (string['d'+ str(i)])
"""

def makeDailyPriceArray(file_path, date):
    """    
    程式的一開始 一定要放
    import pandas as pd 
    不然會執行不了
    
    而且前面要先用 sortDateFromNew 先處理過歷史資料
    # !!! You must import pandas as pd first
    file_path => 放的是歷史資料
    date      => 只要輸入數字, 0 表示最新的資料; 1 表示 前1天; 2表示前 2天
    """    
    
    file_path = str(file_path)
    date = str(date)
    #array_name = str(array_name)
    
    sort_index = 'd' + str(date)
    
    csv_columns = ['code','market','name','industry','start','high','low','end','volumn','daily_money']
    
    pre_array =pd.read_csv(file_path + string[sort_index], encoding = 'utf-8')
    pre_array.columns = csv_columns    
    pre_array['volumn'] = pre_array['volumn'].astype(int) #先把vol換成int
    pre_array = pre_array[pre_array.volumn != 0] #然後在array裡面去掉vol = 0
    #pre_array.index = pre_array['code'] #把index設定成code之後才好合併

    pre_array = pre_array.drop(['industry', 'volumn', 'daily_money'], axis = 1) 
    pre_array = pre_array.rename(columns = {'start' : 'd' + str(date) + '_start','high' : 'd' + str(date) +  '_high', 'low': 'd' + str(date) +  '_low', 'end' : 'd' + str(date) +  '_end'})
       
    array_index = sort_index + '_array'
    #print (array_index)
    return pre_array
    #print (array_name)



d0_array = makeDailyPriceArray(file_path, 0) 
d1_array = makeDailyPriceArray(file_path, 1)
d2_array = makeDailyPriceArray(file_path, 2)
d3_array = makeDailyPriceArray(file_path, 3)
d4_array = makeDailyPriceArray(file_path, 4)

merge_array = pd.merge (d0_array, d1_array, on = ['code' , 'name', 'market'])
merge_array = pd.merge (merge_array, d2_array, on = ['code' , 'name', 'market'])
merge_array = pd.merge (merge_array, d3_array, on = ['code' , 'name', 'market'])
merge_array = pd.merge (merge_array, d4_array, on = ['code' , 'name', 'market'])

print (merge_array.head(10))


#ok, 測試成功, 以後把a 改成 d0_array
"""     
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
#pre_array.index = pre_array['code'] #把index設定成code之後才好合併
d0_array = pre_array
d0_array = d0_array.drop(['industry', 'volumn', 'daily_money'], axis = 1) 
#把不需要的資訊砍了，可是不知道為什麼 axis = 0 是不行的
d0_array = d0_array.rename(columns = {'start' : 'd0_start', 'high' : 'd0_high', 'low': 'd0_low', 'end' : 'd0_end'})
#把始高安終前面加上日期引數 d0 為最靠近的一天
#print (d0_array.head(3))
del pre_array
#print (pre_array)
#date_d0 = history_list[d0]  #這是為了給後面的csv檔有日期
#date_d1 = history_list[d1]
#print (date_d0)
#print (date_d1)
"""

"""
以下是測試d1_array,在合併前先把兩個做出來
"""

"""
pre_array = pd.read_csv(file_path + string['d1'], encoding = 'utf-8')
#d0_array = pre_array.reindex(columns = csv_columns)
#
#d0_array = pd.DataFrame(pre_array, index = range(4000), columns = csv_columns)
pre_array.columns = csv_columns #把col 轉成英文
print (pre_array.columns) #到這裡成功了，接下來是把他拿進新的array
#print (pre_array.head(5)) #我只要code，名，始，高，安，終
#print (d0_array.index)
pre_array['volumn'] = pre_array['volumn'].astype(int) #先把vol換成int
pre_array = pre_array[pre_array.volumn != 0] #然後在array裡面去掉vol = 0
#pre_array.index = pre_array['code'] #把index設定成code之後才好合併
d1_array = pre_array
d1_array = d1_array.drop(['industry', 'volumn', 'daily_money'], axis = 1) #把不需要的資訊砍了，可是不知道為什麼 axis = 0 是不行的
#d0_array = d0_array.reindex(columns = ['code', 'name','d0_start','d0_high','d0_low','d0_end'])
#d1_array = d1_array.rename(columns = {'start' : 'd1_start', 'high' : 'd1_high', 'low': 'd1_low', 'end' : 'd1_end'})
#print (d1_array.head(3))
del pre_array
result = pd.merge (d0_array, d1_array, on = ['code' , 'name', 'market'])
print (result.head(10))
"""
