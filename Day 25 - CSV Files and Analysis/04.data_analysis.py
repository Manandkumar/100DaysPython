import pandas
my_data = pandas.read_csv("./Day 25 - CSV Files and Analysis/2018_Central_Park.csv")
Grey_squ= len(my_data[my_data["Primary Fur Color"] =="Gray"])
Black_squ= len(my_data[my_data["Primary Fur Color"] =="Black"])
Cinnamon_squ= len(my_data[my_data["Primary Fur Color"] =="Cinnamon"])
Grey_squ= len(my_data[my_data["Primary Fur Color"] =="Gray"])
print(f" Count of \n Grey colour:{Grey_squ}\n Black Colour: {Black_squ} \n Cinnamon Color: {Cinnamon_squ}")

data_dic = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [Grey_squ,Black_squ,Cinnamon_squ]
}

data = pandas.DataFrame(data_dic)
data.to_csv("./Day 25 - CSV Files and Analysis/2018CentralPark_Analysis.csv")
