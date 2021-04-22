import csv
import HashTable

distance_hash_ref = HashTable.HashTable()

with open('WGUPSDistanceTable.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        package = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], 'At Hub', row[7]]

        distance_hash_ref.insert()
