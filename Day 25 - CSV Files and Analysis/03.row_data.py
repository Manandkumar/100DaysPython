# get row data 
import pandas
my_data = pandas.read_csv("./Day 25 - CSV Files and Analysis/weather_data.csv")
print(my_data[my_data["Condition"]=="Rainy"])
setMax= my_data["Temperature"].max()
print(my_data[my_data["Temperature"]==setMax])
