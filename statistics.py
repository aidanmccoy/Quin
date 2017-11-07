import pandas
import decimal

#Returns the average of the ratios of male to female populations. 
def getAvg(data, numEntries):

  ratioTotal = decimal.Decimal(0)

  for i in range(numRows):
    ratioTotal += decimal.Decimal(data.at[i, 'TOT_MALE']) / decimal.Decimal(data.at[i, 'TOT_FEMALE'])

  return ratioTotal / decimal.Decimal(numEntries)

def getStandardDev(data):

data = pandas.read_csv("gallatinPopulation.csv")
numRows,numCols=data.shape

print("The average ratio is:", getAvg(data, numRows))