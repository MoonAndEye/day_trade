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
import time

#之後要用diction加上迴圈

start_time = time.time()
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
    pre_array['start'] = pre_array['start'].astype(float)
    pre_array['high'] = pre_array['high'].astype(float)
    pre_array['low'] = pre_array['low'].astype(float)
    pre_array['end'] = pre_array['end'].astype(float)
    pre_array = pre_array.drop(['industry', 'volumn', 'daily_money'], axis = 1) 
    pre_array = pre_array.rename(columns = {'start' : 'd' + str(date) + '_start','high' : 'd' + str(date) +  '_high', 'low': 'd' + str(date) +  '_low', 'end' : 'd' + str(date) +  '_end'})
       
    #array_index = sort_index + '_array'
    #print (array_index)
    return pre_array
    #print (array_name)


date_array = {}
merge_base = ['code' , 'name', 'market']#這個放要合併基準
# date_array[0] 就是最靠新資料的DataFrame
# 如果要改計算天數，就改下面這個range的數字, 22是月
for i in range (5):
    date_array[i] = makeDailyPriceArray(file_path, i) 
    #這個i不能把他當成string
    if i == 0:
        pass
    elif i == 1:
        merge_array = pd.merge (date_array[0], date_array[1], on = merge_base)
    else :
        merge_array = pd.merge (merge_array, date_array[i], on = merge_base)

#cal_array = merge_array['code', 'market', 'name']
#cal_array = merge_array [['code', 'market', 'name']]
merge_array ['w_highest'] = merge_array[['d0_high','d1_high', 'd2_high', 'd3_high', 'd4_high',]].max(axis = 1)
merge_array ['w_lowest'] = merge_array[['d0_low','d1_low', 'd2_low', 'd3_low', 'd4_low',]].min(axis = 1)

merge_array ['d0_range'] = merge_array['d0_high'] - merge_array['d0_end']
merge_array ['d1_range'] = merge_array['d1_high'] - merge_array['d1_end']
merge_array ['d2_range'] = merge_array['d2_high'] - merge_array['d2_end']
merge_array ['d3_range'] = merge_array['d3_high'] - merge_array['d3_end']
merge_array ['d4_range'] = merge_array['d4_high'] - merge_array['d4_end']

merge_array ['d0_indicate'] = merge_array['d0_high'] + merge_array['d0_end']
merge_array ['d1_indicate'] = merge_array['d1_high'] + merge_array['d1_end']
merge_array ['d2_indicate'] = merge_array['d2_high'] + merge_array['d2_end']
merge_array ['d3_indicate'] = merge_array['d3_high'] + merge_array['d3_end']
merge_array ['d4_indicate'] = merge_array['d4_high'] + merge_array['d4_end']

merge_array ['d_widest'] = merge_array[['d0_range','d1_range', 'd2_range', 'd3_range', 'd4_range',]].max(axis = 1)
merge_array ['d_indicate'] = merge_array[['d0_indicate','d1_indicate', 'd2_indicate', 'd3_indicate', 'd4_indicate',]].max(axis = 1)

merge_array ['average'] = merge_array[['d0_end','d1_end', 'd2_end', 'd3_end', 'd4_end',]].mean(axis = 1)


merge_array ['index1'] = merge_array ['d_widest'] / merge_array ['average']
merge_array ['index2'] = merge_array ['d_widest'] / merge_array ['d_indicate']


merge_array ['index3'] = (merge_array ['w_highest'] - merge_array ['w_lowest'] ) / merge_array ['average']
merge_array ['index4'] = (merge_array ['w_highest'] - merge_array ['w_lowest'] ) / (merge_array ['w_highest']+ merge_array ['w_lowest'] )
"""
# 如果要看排序 就把這行註解取消掉
cal_array = cal_array.sort(['index2'], ascending=[False])
"""
#pd.set_option('display.precision',20)
#print (merge_array[:10]) #可以試著寫成這個，從前面數十個


want_printout =['code', 'name','market', 'w_highest', 'w_lowest', 'average', 'index1', 'index2', 'index3', 'index4' ]
#以後要改就改 want_printout
cal_array = merge_array.loc[:,want_printout]

#print (cal_array[:10])

only1_array = cal_array[cal_array['market'].str.contains("1")]
print (cal_array[:10]) 

#print (only1_array[:10])

#ok, 測試成功, 以後把a 改成 date_array[0]

#header = cal_array.columns
#write_in = cal_array.to_csv(encoding = 'utf-8')
#print (header)
cal_array.to_csv('C:/1save/jpStock/dayTrade/' + string['d0'], encoding = 'utf-8')

print("Run time --- %s seconds ---" % (time.time() - start_time))

