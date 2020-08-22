import csv


# CONSTANTS
FILENAME = 'employees.csv'

with open(FILENAME, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)