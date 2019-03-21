# Written for Python3 in Jupyter Notebooks on PTDataX

# Library Imports
import pandas as pd
import numpy as np

# Web requests/curl 
import requests

import csv
#import urllib2

# Ref: https://stackoverflow.com/questions/35371043/use-python-requests-to-download-csv

url = 'http://chords.tacc.cloud/instruments/5.csv?start=2019-01-04T00:30&end=2019-03-15T12:30'
filename = 'datatree_test5.csv'
r = requests.get(url)
# Removes the byte formating (b'') of the request
decoded_r = r.content.decode('utf-8')
# Reads the request data in as a csv object
cr = csv.reader(decoded_r.splitlines(), delimiter=',')
# converts the CSV object into a list
mylist = list(cr)
# makes a seperate list for the data header
headers = mylist[13]
# drops the data list into a dataframe
datatree_data = pd.DataFrame(mylist)

datatree_data.columns = headers
datatree_data.set_index('Time')
datatree_ready = datatree_data.iloc[14:]
datatree_ready.set_index('Time')
