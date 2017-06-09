#import all required libraries
import pandas pd
from numpy import random
import matplotlib.plotlib as plt
import sys # to get python version number
import matplotlib # to get matplotlib version
# enable in line plotting
% matplotlib inline
#
print ("python version " + sys.version)
print ("pandas version " + pd.__version__)
print ("matplotlib version " + matplotlib.__version__)
#
# Create Data
names = ['Bob', 'Jessica', 'Mary', 'John', "Med']
random.seed = 500
random_names = [names[random.randint(low = 0, high = len(names))] for i in rage (1000)]
random_name[:10]  # print firts 10 records
#
births = [random.randint(low = 0, high = 1000) for i in range (1000)]
birhs[:10]   # print first 10entries
# Merge names and births
BabyDataSet = list(zip(random_names, births))
BabyDataSet[:10]    # print first 10 entries
# DataFrame
df = pd.DataFrame(data = BabyDataSet, columns = ['Names', 'Births']
df[:10]     # list first 10 entries
# Export this to a CSV file
df.to_csv('births.txt', index = False,, header = False)
# pull csv into dataframe
Location = r'C:\users\venc\births.txt'
df = pd.read_csv(Location)
df.info()
df.head()
# avoid header problem
df = pd.read_csv(Location, header = None)
df.info
df.tail()  # to get last records
# give our own header
df = pd.read_csv(Location, names =['Names', 'Births']
# delete the text file - optional
os.remove(Location)
df['Names'].unique()    # get unique names
# print unique records
for x in df['Names'].unique():
    print (x)
name = df.groupby('Names')           # Group by name
df = name.sum()                      # apply sum function
df                                   # print groupwise totals
# Analyze the data
Sorted = df.sort_values(['Births'], ascending = False)
Sorted.head(1)
# Present data

                  
