#!/usr/bin/python
# coding=<utf-8>

# Import libraries
import csv
import json

## READING FROM CSV

# Variable to store list of rows
records = []

# Open CSV file for reading and add rows to list of rows
with open("vehicles.csv", "r") as file:
  reader = csv.reader(file)
  for row in reader:
    print("Row", row) 
    records.append(row)

# Print vehicles_list to see the object returned by the csv reader.
print('VEH_LIST:', records)

# Convert the record entries into a list of dictionaries
# to be written in a JSON file.

new_records = []

for record in records:
  print("Raw record:", record)

for record in records:
    record_dict = {}
    record_dict["type"]   = record[0]
    record_dict["make"]   = record[1]
    record_dict["model"]  = record[2]
    record_dict["year"]   = record[3]
    record_dict["colour"] = record[4]
    record_dict["price"]  = record[5]

    print("Dict record:", record_dict)
    new_records.append(record_dict)

print('\nNEW_LIST:', new_records)


## WRITING TO JSON

# Open a JSON file for writing and write list of new records.

json_string = json.dumps(new_records, indent=4, sort_keys=True)
print(json_string)

with open("vehicles.json", "w") as file:
    file.write(json_string)
  

## READING FROM JSON

# Retrieve the data from the JSON file and
# add records to a list to be written in new CSV file

# Open a JSON file for reading and read the data to a variable
with open("vehicles.json", "r") as file:
    json_data = json.load(file)

print(json_data)

  # Use list comprehension to create a list of lists of values
  # corresponding to the information for each vehicle
  
new_vehicles = [list(record.values()) for record in json_data]


  


## WRITING TO CSV

# Open a new CSV file for writing and write all the vehicle records

with open("new_vehicles.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(new_vehicles)