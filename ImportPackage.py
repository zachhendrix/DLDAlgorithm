# Imports data from the 'WGUPSPackageFile' csv file and hashes it in the 'package_hash' hash table
# The 'package' list is created from data in the rows and the list is inserted into the 'package_hash'
import csv
import HashTable

package_hash = HashTable.HashTable()

# Time Complexity O(N)
def import_packages():
    for x in range(1, len(package_hash.table)):
        package_hash.remove(x)

    # Time Complexity O(N)
    with open('WGUPSPackageFile.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Requirement E: Objects inserted using package id as the key
        for row in csv_reader:
            package = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], 'At Hub', row[7]]

            package_hash.insert(row[0], package)
