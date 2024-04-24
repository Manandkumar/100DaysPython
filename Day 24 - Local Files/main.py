# with open ("./Day 24 - Local Files/Letters/startng_letter.txt","w") as mail:
#     mail.write("Dear [Name], \nI am writing to extend our sincere invitation for you to join us at the upcoming symposium on [theme] hosted by our esteemed organization.\nThe symposium will be held on [date] at [venue] and will feature a diverse range of experts sharing their insights on the latest developments in [field].\nRegards,\nAnand Kumar\n")

# with open ("./Day 24 - Local Files/Names/invited_names.txt","w") as senders:
#     senders.writelines("Anand Mitul Ahaan")

PLACEHOLDER ="[Name]"
THEME ="[theme]"
DATE = "[date]" 
VENUE = "[venue]" 


with open("./Day 24 - Local Files/Names/invited_names.txt") as names_file:
    names= names_file.readlines()
    print(names)

with open("./Day 24 - Local Files/Letters/starting_letter.txt") as letter_file:
    contents= letter_file.read()
    print(contents)
    for name in names:
        stripped_name=name.strip()
        new_letter=contents.replace(PLACEHOLDER,stripped_name).replace("[venue]","My Home").replace("[date]", "28.04.2024").replace("[theme]", "Minecraft").replace("[field]", "Time wasting approach")
        with open(f"./Day 24 - Local Files/Output/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
