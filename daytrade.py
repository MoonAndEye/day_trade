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

history_list = []
for name in os.listdir('C:/1save/jpStock/raw'):
    history_list.append(name)

#可能要從這邊建立,比較符合python的語法
#把他寫成 def
history_number = int(len(history_list)) - 1
string = {}
for i in range(0, 9):
  string['d' + str(i)] = history_list[history_number]
  history_number = history_number - 1

"""
#下面這一行,是用來排序array 平常不需要用
b = OrderedDict(sorted(string.items()))

print (b) 
print (string[key])
"""


def sortDataFromNew (source_list):
    history_number = int(len(source_list)) - 1


#d0 = history_number -1 #要射的飛標只要這個
#d1 = history_number -2
#d2 = history_number -3
#d3 = history_number -4
#d4 = history_number -5

#date_d0 = history_list[d0]  #這是為了給後面的csv檔有日期
#date_d1 = history_list[d1]
#print (date_d0)
#print (date_d1)
