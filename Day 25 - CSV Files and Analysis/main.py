import csv
with open("./Day 25 - CSV Files and Analysis/weather_data.csv") as my_file:
    contents= csv.reader(my_file)
    temperature =[]
    for row in contents:
        if row[1]!= "Tem":
            temperature.append(int(row[1]))
        print(row)
    print (temperature)

import pandas