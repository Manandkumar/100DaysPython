import csv
with open("./Day 25 - CSV Files and Analysis/weather_data.csv") as my_file:
    contents= csv.reader(my_file)
    for row in contents:
        print(row)