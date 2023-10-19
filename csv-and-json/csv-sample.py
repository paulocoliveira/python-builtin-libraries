import csv

# Reading data from a CSV file
with open('test_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Writing data to a CSV file
data_to_write = [['Name', 'Age'], ['John Doe', '30'], ['Jane Smith', '25']]

with open('output_data.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data_to_write)
