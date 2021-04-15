import csv
import HashTable

csvHashRef = HashTable.ChainingHashTable()
with open('WGUPSPackageFile.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineCount = 0
    for row in csv_reader:
        objectid = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        deadline = row[5]
        weight = row[6]
        status = "At Hub"
        message = row[7]
        package = (objectid, address, city,state, zipcode, deadline, weight, status, message)

        csvHashRef.insert(package)