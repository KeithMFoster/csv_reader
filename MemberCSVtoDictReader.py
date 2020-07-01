import csv
import sys
import pprint
import datetime
import operator

reader = csv.DictReader(open('Protech Member Query V4.csv', 'rb'))
dict_list = []
for line in reader:
    dict_list.append(line)

pprint(dict_list)