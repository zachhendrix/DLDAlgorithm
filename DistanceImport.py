import csv
import HashTable

distance_table = []

with open('WGUPSDistanceTable.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        distance = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15],
                    row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23]]
        distance_table.insert(0, distance)
