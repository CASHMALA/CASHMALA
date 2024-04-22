import csv
import pandas
import statistics
tottemp = 0
with open("myfile3.csv", "r", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader, None)

    line = csvfile.readline()
    print(line, "readline1")
    columns = line.strip().split(',')
    column1 = columns[0]
    tottemp += int(column1)
print("tottemp", tottemp)
