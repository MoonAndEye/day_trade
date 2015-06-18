# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:56:39 2015

"""
import os, random, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from pympler.asizeof import asizeof

obj = pd.Series([1,3,5,np.nan,6,8])

test = []
test2d = []
for i in range(5):
    test.append(random.randint(1,10))    
    test2d.append(test)

test.append (None)
test.append (23)

s = pd.Series(test)
#print (s)

for i in range(len(test)):
    if test[i] == 23:
        test.pop(i)

#print (test)

#file = open('C:/1save/jpStock/raw/2015-06-16c.csv', encoding = 'shift-jis')

file = 'C:/1save/jpStock/raw/2015-06-16.csv'

with open(file, 'r', encoding = 'shift-jis') as fin:
    data = fin.read().splitlines(True)
    #data1 = data[1:]
    cc = data[1]
    content = data[2:]

file1 = 'C:/1save/test.csv'

#pd.concat([df1, df4], axis=1) 這是拿來合併表格用的

with open(file1, 'w', encoding = 'utf-8') as found:
    found.writelines(cc)
    found.writelines(content)

test1 = pd.read_csv(file1)   

print (test1.columns) 
"""
#print (data)
#with open(file, 'w') as fout:
#    fout.writelines(data[1:])
index_array = []
#index1 = pd.Index(range(len(content)), name = 'foo')
for i in range(len(content)):
    index_array.append(str(i))
#print (index)

test1 = pd.DataFrame(content, index = index_array, columns = cc)

print (test1)

#file.close()
"""

"""
print (sys.getsizeof(test))
print (test)
print (sys.getsizeof(test2d))
print (test2d)
"""

#print (asizeof(obj))
"""
print (pandas.pnow('D'))
#print (pd.period(year = 2016, month = 6, day=17, freq = 'D'))
#p = pandas.period_range('1985', '2010', freq = 'B')
#print (dir(pandas))

#print (p)
#print (p.asfreq('D', 'start'))

rng = pandas.period_range('1987Q2', periods=10, freq='Q-DEC')
data = pandas.Series(np.random.randn(10), index=rng)
plt.figure(); data.plot()

"""
"""
import benefit_calculate
exec('benefit_calculate')
"""
