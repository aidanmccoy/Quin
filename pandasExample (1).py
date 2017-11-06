# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 09:33:18 2014

@author: jheys
"""

import numpy
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("gallatinPopulation.csv")
numRows,numCols=data.shape

print(data.columns)
print(data.values)

getAvg(data, numRows)

def getAvg(data, numEntries):

  ratioTotal = 0

  for i in range(numRows):
    avg += (data.at[i, 'TOT_MALE'] + data.at[i, 'TOT_FEMALE'])

  return ratioTotal / numEntries



# stats=data.describe()
# print(stats)

# print(stats.mean(TOT_MALE))
# print(stats.std())
# print(stats(4,2))

# def MaleParse(data):
#     Maledata=numpy.zeros(numRows)
#     for i in range(numRows):
#         Maledata=data()
#     return Maledata

# Male1=MaleParse(data)
# print(Male1)

# def getTotMale(data,year):
#     countYear=0
#     for i in range(numRows):
#         if(data[i,2]==year):
#             countYear +=1
#     Maledata=numpy.zeros(countYear)
#     countYear=0
#     for i in range(numRows):
#         if (data[i,2]==year):
#             Maledata[countYear]=data[i,4]
#             countYear+=1
#     return Maledata

#Male1=getTotMale(data,1)
#print(Male1.mean())
 #   countMale=numpy.count_nonzero(data[:,4]==male)
  #  Maledata=numpy.zeros(countMale)
   # countMale=0
    #for i in range(numRows):
     #   if (data[i,4]==male):
      #      Maledata[countMale]=data[i,2]
       #     countMale+=1
    #return Maledata

#num=getTotMale(data,1)
#print(num.mean())



#plt.hist(data.TOT_MALE,10)

#def averageGenRat (data):
 #   for i in range (numRows):
        

#print(data.sort_values(by='DO'))
#print(data.Temp > 26.0)

# Plot a histogram of temperatures
#plt.hist(data.Temp,9)
#plt.title("Distribution of Temperature Measurements")
#plt.xlabel("Temperature ($^oC$)")
#plt.ylabel("Frequency")
#plt.savefig('tempHistogram.png',dpi=150)

# T-test
#t, prob = scipy.stats.ttest_ind(DOdata1,DOdata2,equal_var = True)
#print(t)
#print(prob)

# Z-scores
#zscore = scipy.stats.zscore(DOdata1)
#print(zscore)

    
