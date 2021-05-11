import csv

distance_table = []

with open('WGUPSDistanceTable.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        distance_table.append(row)


