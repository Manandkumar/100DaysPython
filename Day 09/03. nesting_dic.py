# nesting

capitals ={
    "India": "New Delhi",
    "Germany": "Berlin",
    "France":"Paris"
}

#nesting a list in dictory

travel_log ={
 "France":["Paris","Lille", "Dijon"],
  "India":{"cities_visited": ["Hyderabad","Bangalore","Chennai","Pune", "Ahmedabad" ],"total_visited":12}
}


#nesting a dictionary in a list 
travel_log2 =[
 {"country": "france",
  "cities visited": ["Paris","Lille", "Dijon"],
 },
 {
     "country":"India",
     "cities_visited":["Hyderabad","Bangalore","Chennai","Pune","Ahmedabad"],
     "total_visited":12

 }
  
]


def add_new_country(country,No_of_visits,list_of_cities):
    new_country={}
    new_country["country"] = country
    new_country["visits"] = No_of_visits
    new_country["cities"] =list_of_cities
    travel_log2.append(new_country)


country = str(input("Enter the country you visited: "))
No_of_visits = int(input("Enter the number of times you visited the country : "))
list_of_cities = str(input("Enter the cities you have visited with coma: "))

add_new_country(country,No_of_visits,list_of_cities)


print(travel_log2)


