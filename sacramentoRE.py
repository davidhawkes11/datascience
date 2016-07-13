import csv
import requests
import os
import sys

CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

with requests.Session() as s:
    download = s.get(CSV_URL)

    line_iterator = (x.decode('utf-8') for x in download.iter_lines(decode_unicode=True))

    cr = csv.reader(line_iterator, delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)
