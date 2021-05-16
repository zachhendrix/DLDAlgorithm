# Imports data from the 'WGUPSDistanceTable' csv file and caches it in the 'distance_table' list.
# The distances are used by comparing two addresses via index from the WGUPSAddressTable.
import csv

distance_table = []

with open('WGUPSDistanceTable.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        distance_table.append(row)


