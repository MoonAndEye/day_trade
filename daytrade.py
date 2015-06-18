# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:35:05 2015

@author: Moon
"""

import os, random, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

history_list = []
for name in os.listdir('C:/1save/jpStock/raw'):
    history_list.append(name)
    
history_number = int(len(history_list))

for i in range(5):
    'd'+i

#d0 = history_number -1 #要射的飛標只要這個
#d1 = history_number -2
#d2 = history_number -3
#d3 = history_number -4
#d4 = history_number -5

date_d0 = history_list[d0]  #這是為了給後面的csv檔有日期
date_d1 = history_list[d1]
print (date_d0)
#print (date_d1)

