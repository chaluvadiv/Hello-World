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
