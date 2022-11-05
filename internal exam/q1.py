import random
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("1305x652")
root.config(pady=100,padx=100)

listbox = Listbox(root, height=20, width=50)

def theme():
    color = ["blue", "red", "green", "yellow", "orange",
             "pink", "purple", "brown", "grey", "black"]
    a = random.choice(color)
    root.config(bg=a)

#  function to validate the fields


def insert():

    if entryfirst.get() == "" or entrylast.get() == "" or entryemail.get() == "" or entryzip.get() == "":
        messagebox.showerror("Error", "Please fill first name / last name / email / zip")
        return

    for char in entryfirst.get():
        if char.isdigit():
            messagebox.showerror("Error", "First Name should not contain numbers")
            return
    
    for char in entrylast.get():
        if char.isdigit():
            messagebox.showerror("Error", "Last Name should not contain numbers")
            return
    
    if not entryemail.get().__contains__("@"):
        messagebox.showerror("Error", "Invalid Email")
        return
    
    if not entryzip.get().isdigit():
        messagebox.showerror("Error", "Invalid Zip Number")
        return

    global listbox
    listbox.insert(END,"First name : " + entryfirst.get() + "| Last Name : " + entrylast.get() + " | Email : " + entryemail.get() + " | zip : " + entryzip.get()) 
    messagebox.showinfo("Insert", "Inserted Successfully")

def delete():
    try :
        listbox.delete(listbox.curselection())
        messagebox.showinfo("Delete", "Deleted Successfully")
    except:
        messagebox.showerror("Error", "Please select a record to delete")
    


first_name = StringVar()
last_name = StringVar()

gender = IntVar()
language = IntVar()
email = StringVar()
state = StringVar()
address = StringVar()
zip = IntVar()
creditCardType = StringVar()


lfirst = Label(root, text="First Name :")
entryfirst = Entry(root)
# place the label and entry
lfirst.grid(row=0, column=0)
entryfirst.grid(row=0, column=1)

llast = Label(root, text="Last Name :")
entrylast = Entry(root)
# place the label and entry
llast.grid(row=1, column=0)
entrylast.grid(row=1, column=1)

gender = Label(root, text="Gender :")
radiomale = Radiobutton(root, text="Male", value=1, variable=gender)
radiofemale = Radiobutton(root, text="Female", value=2, variable=gender)
# place the radio buttons
gender.grid(row=2, column=0)
radiomale.grid(row=2, column=1)
radiofemale.grid(row=2, column=2)

language = Label(root, text="Language :")
checkenglish = Checkbutton(root, text="English")
checkhindi = Checkbutton(root, text="Hindi")
checktelugu = Checkbutton(root, text="Telugu")
# place the label and checkbuttons
language.grid(row=3, column=0)
checkenglish.grid(row=3, column=1)
checkhindi.grid(row=3, column=2)
checktelugu.grid(row=3, column=3)


lemail = Label(root, text="Email :")
entryemail = Entry(root)
# place the label and entry
lemail.grid(row=4, column=0)
entryemail.grid(row=4, column=1)

laddress = Label(root, text="Address :")
entryaddress = Text(root, height=5, width=20)
# place the label and entry
laddress.grid(row=5, column=0)
entryaddress.grid(row=6, column=1)

lstate = Label(root, text="State :")
# give a dropdown list
state.set("Select State")
state_list = OptionMenu(root, state, "Andhra Pradesh",
                        "Telangana", "Karnataka", "Tamil Nadu")
# place the label and dropdown list
lstate.grid(row=8, column=0)
state_list.grid(row=8, column=1)

lzip = Label(root, text="Zip Code :")
entryzip = Entry(root, validate="key")
# place the label and entry
lzip.grid(row=9, column=0)
entryzip.grid(row=9, column=1)

lcreditCardType = Label(root, text="Credit Card Type :")
# give a dropdown list
creditCardType.set("Select Credit Card Type")
creditCardType_list = OptionMenu(root, creditCardType, "Visa",
                                 "Master Card", "American Express")
# place the label and dropdown list
lcreditCardType.grid(row=10, column=0)
creditCardType_list.grid(row=10, column=1)

# theme button
theme = Button(root, text="Theme", command=theme)
theme.grid(row=4, column=5,padx=200)

# insert button
button = Button(root, text="Insert", command=insert)
button.grid(row=6, column=5,padx=200)

# delete button
button = Button(root, text="Delete", command=delete)
button.grid(row=8, column=5,padx=200)

lbillibg = Label(root, text="Billing Records",font=("Arial", 20, "bold"),bg="grey")
# place the label and listbox
lbillibg.grid(row=0, column=20, columnspan=2)
listbox.grid(row=1, column=20, rowspan=10, columnspan=2)


root.mainloop()
