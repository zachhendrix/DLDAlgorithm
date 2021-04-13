import csv

with open('./projectdata/WGUPS Package File.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')



packageList ={'ID': '0', 'Address': '', 'Deadline': '', 'City': '', 'Zipcode': '', 'Weight': '', 'Status': ''}
