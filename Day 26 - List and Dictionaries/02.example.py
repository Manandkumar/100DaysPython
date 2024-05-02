range_list =[num*2 for num in range(1,5)]
print (range_list)

# conditioanl List comprehension 

new_list = [num*3 for num in range(1,10)]
print(new_list)

names =['anand', 'ahaan', 'aruni', 'chinnu']

short_name = [name for name in names if len(name)<=5]

print(short_name)