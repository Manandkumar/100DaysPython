from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=300)
window.config(padx=10,pady=10)

def button_click():
    miles = float(MyMiles.get())
    km = miles*1.609
    MyLabel3.config(text=km)

#input box
MyMiles = Entry(width=5)
MyMiles.grid(row=0,column=1)

#label 
MyLabel1 = Label(text="Miles ",font=("Arial",12))
MyLabel1.grid(row=0,column=2)

#label 

MyLabel = Label(text="is equal to ",font=("Arial",12))
MyLabel.grid(row=1,column=1)


#label 

MyLabel2= Label(text="Km ",font=("Arial",12))
MyLabel2.grid(row=1,column=2)

#button
Mybutton = Button(text="Caluculate",command=button_click)
Mybutton.grid(row=2,column=1)

#label 
MyLabel3 = Label(text=" 0 ",font=("Arial",12))
MyLabel3.grid(row=1,column=2)


window.mainloop()