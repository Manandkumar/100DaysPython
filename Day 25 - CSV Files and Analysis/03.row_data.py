# get row data 
import pandas
my_data = pandas.read_csv("./Day 25 - CSV Files and Analysis/weather_data.csv")
print(my_data[my_data["Condition"]=="Rainy"])
setMax= my_data["Temperature"].max()
print(my_data[my_data["Temperature"]==setMax])

#create a dataframe

data_dict ={
    "student": ['anand', 'mitul', 'ahaan'],
    "scores":[76,56,86]
}

data= pandas.DataFrame(data_dict)
print(data)
data.to_csv("./Day 25 - CSV Files and Analysis/new_data.csv")
