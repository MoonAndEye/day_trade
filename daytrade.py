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

file_path = 'C:/1save/jpStock/raw' #檔案路徑的代號，這邊放歷史資料
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
print (string['d0'])

#d0 = history_number -1 #要射的飛標只要這個
#d1 = history_number -2
#d2 = history_number -3
#d3 = history_number -4
#d4 = history_number -5

#date_d0 = history_list[d0]  #這是為了給後面的csv檔有日期
#date_d1 = history_list[d1]
#print (date_d0)
#print (date_d1)
