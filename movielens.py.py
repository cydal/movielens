__author__ = 'sijuade'

import csv


filename = "C:\Users\sijuade\Downloads\ml-100k\ml-100k\u.item"
output = open('uitem.csv', 'wb')



with open(filename, 'rb') as f:
    csvread = csv.reader(f, delimiter='\t')
    writer = csv.writer(output)

    for row in csvread:
        line = row[0].strip().split('|')
        writer.writerow(line)