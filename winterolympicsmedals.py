"""
import urllib.request
with urllib.request.urlopen('http://vtr.aec.gov.au/HouseCandidates-20499.htm') as f:
	print(f.read(500))
"""
import csv
import urllib.request
"""
url = 'http://vtr.aec.gov.au/HouseCandidates-20499.htm'
response = (urllib.request.urlopen(url))
reader = (csv.reader(response))

for row in reader:
    print (row)
"""
    
"""
import csv
with open('C:/Users/David/Downloads/medals.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
"""

with open('C:/Users/David/Downloads/medals.csv') as ifile:
    read = csv.reader(ifile) 
    for row in read:
        print (row) 
