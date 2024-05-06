from tkinter import *

window = Tk()
window.title("Multiple Items")
window.minsize(width=600,height=400)

def click_button():
    print(" You have clicked the button!")
    my_label.config(text=" Button is Clicked!!",font=("Arial",12,"italic") )

# Labels

my_label = Label(text="Sample Text")
my_label.pack()

#button 
my_button = Button(text="Click Me!",command=click_button)
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

# scroll
def spinbox_used():
    print(my_spin.get())

my_spin= Spinbox(from_=0,to=10, width=10,command=spinbox_used)
my_spin.pack()

#scale

def scaled_used():
    print(my_scale.get())

my_scale = Scale(from_=0, to=100, command=scaled_used)
my_scale.pack()

#checkbox

def checkbox_used():
    print(checked_state.get())

checked_state =IntVar

my_checkbox = Checkbutton(text="Is on?", variable=checked_state, command=checkbox_used)
checked_state()

my_checkbox.pack()

#radio button 
def radio_used():
    print(radio_state.get())
radio_state = IntVar()

my_radio1= Radiobutton(text="Option 1", value=1, command=radio_used)
my_radio1.pack()


#list box 
def list_used(event):
    print(my_list.curselection())
radio_state = IntVar()

my_list = Listbox(height=5)
fruits = ["apple", "mango", "Pine apple", "Ice Apple"]
for fruit in fruits:
    my_list.insert(fruits.index(fruit), fruit)
my_list.bind("<<Listbox Select>>",list_used)
my_list.pack()



window.mainloop()
