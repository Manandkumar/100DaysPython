import pandas

data= pandas.read_csv("./Day 25 - CSV Files and Analysis/weather_data.csv")
print(type(data["Day"]))
data_dic = data.to_dict()
temp = data["Temperature"].to_list()
print(data_dic)
print(sum(temp),sum(temp)/len(temp))

max_temp = max(data["Temperature"])


print(f"The Maximum temperature from the list is: {max_temp}")
print(data["Temperature"].mean())