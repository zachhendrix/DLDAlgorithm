# Imports data from the 'WGUPSAddressTable' csv file and caches it in the 'address_table' list.
# The addresses are used as an index to determine distance with the help of the WGUPSDistanceTable.
import csv

address_table = []

# Time Complexity O(N)
with open('WGUPSAddressTable.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        address_table.extend(row)
