import csv
import HashTable

class Package:
    def __init__(self,objectid,address,city,state,zipcode,deadline,weight,status,message):
        self.objectid = objectid
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.message = message


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
        package = Package(objectid, address, city,state, zipcode, deadline, weight, status, message)

        csvHashRef.insert(package)
