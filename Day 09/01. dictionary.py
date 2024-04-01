anand_family = {
    "father": "Anand", 
    "mother":"Mitul",
    "son": "Ahaan",
}
item =0
items = int(len(anand_family))
print(items)
anand_family["grand_fahter"]="Vijaya Kumar"   
anand_family["grand_mother"]="Kalavathi"   
anand_family["Uncle"]="Anil Kumar"   
anand_family["Aunt"]="Archana"   

print(anand_family)
print(anand_family["Aunt"])

#edit an item
anand_family["M_Grand_father"]= "Ashok Kumar"
anand_family["M_Grand_mother"]= "Ranjana"

print(anand_family)

for key in anand_family:
    print(f"{key} and : {anand_family[key]}")


