import csv
import HashTable


package_hash = HashTable.HashTable()

with open('WGUPSPackageFile.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        package = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], 'At Hub', row[7]]

        package_hash.insert(row[0], package)
