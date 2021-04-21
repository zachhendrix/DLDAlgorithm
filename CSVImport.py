import csv
import HashTable
import Package

csvHashRef = HashTable.ChainingHashTable()

with open('WGUPSPackageFile.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineCount = 0
    for row in csv_reader:
        package = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], 'At Hub', row[7]]

        csvHashRef.insert(row[0], package)
