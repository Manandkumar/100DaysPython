from tkinter import *

window = Tk()
window.title("Multiple Items")
window.minsize(width=600,height=400)

# Labels

my_label = Label(text="Sample Text")
my_label.pack()

#button 
my_button = Button(text="Click Me!")
my_button.pack()

#entries

my_entry = Entry(width= 100)
my_entry.insert(END, string= "Some text to begin with")
print(my_entry.get())
my_entry.pack()

# Text 
my_text = Text(height=5, width=10)
my_text.focus()
my_text.insert(END,"Example of multi line text entry")

my_text.pack()









window.mainloop()
