import csv

address_table = []

with open('WGUPSAddressTable.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        address_table.append(row)
