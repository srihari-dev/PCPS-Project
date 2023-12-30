# Import all the necessary modules
from tkinter import *
from tkinter import messagebox
from AddModule import *
from EditModule import *
from DeleteModule import *
from SearchModule import *
from DisplayModule import *
from WipeModule import *
import datetime as date
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
date = date.datetime.now()
label = customtkinter.CTkLabel(root, text=f"{date:%A, %B %d, %Y}")
label.pack(side=TOP,pady=10)
root.title("PHONE BOOK APPLICATION")
root.geometry("600x550")
root.maxsize(600, 550)
root.minsize(600, 550)
customtkinter.CTkLabel(root, text="PHONE BOOK APPLICATION", font=("Futura", 25)).pack(side=TOP, pady=10)
customtkinter.CTkLabel(root, text="SELECT ONE OF THE GIVEN OPTIONS:", font=("Comic Sans", 15)).pack(side=TOP, pady=10)

def clickb1():
    w = customtkinter.CTkToplevel(root)
    w.wm_title("Add Contacts")
    w.wm_transient(root) #Makes w appear on top of main window
    label1 = customtkinter.CTkLabel(w, text="Enter name: ")
    e1 = customtkinter.CTkEntry(w)
    label2 = customtkinter.CTkLabel(w, text="Enter Phone Number(ten digits): ")
    e2 = customtkinter.CTkEntry(w)

    def success():
        if add(e1.get(), e2.get()) == True:
            messagebox.showinfo("Message", "SUCCESSFULLY ADDED ENTRY!")
            w.destroy()
        elif add(e1.get(), e2.get()) == False:
            messagebox.showinfo("Error", "Please enter phone number in the correct format")
        elif add(e1.get(), e2.get()) == "alreadyexists":
            messagebox.showinfo("Error", "Someone with this name or number already exists in the directory")

    b = customtkinter.CTkButton(w, text="SUBMIT", command=success)
    label1.grid(row=0, column=0, padx=10, pady=10)
    e1.grid(row=0, column=2, padx=10, pady=10)
    label2.grid(row=1, column=0, padx=10, pady=10)
    e2.grid(row=1, column=2, padx=10, pady=10)
    b.grid(row=3, column=1, padx=10, pady=10)
    w.mainloop()

def clickb2():
    w = customtkinter.CTkToplevel(root)
    w.wm_title("Update Contacts")
    w.wm_transient(root) #Makes w appear on top of main window
    label1 = customtkinter.CTkLabel(w, text="Enter name of person whose number must be changed: ")
    e1 = customtkinter.CTkEntry(w)
    label2 = customtkinter.CTkLabel(w, text="Enter New Phone Number(10 digits): ")
    e2 = customtkinter.CTkEntry(w)

    def success():
        if edit(e1.get(), e2.get()) == True:
            messagebox.showinfo("Message", "SUCCESSFULLY EDITED PHONE NUMBER!")
            w.destroy()
        elif edit(e1.get(), e2.get()) == False:
            messagebox.showinfo("Error", "No such person exists in the directory")
        elif edit(e1.get(), e2.get()) == "invalid":
            messagebox.showinfo("Error", "The new number you have entered is invalid\nPlease enter a 10 digit number")

    b = customtkinter.CTkButton(w, text="SUBMIT", command=success)
    label1.grid(row=0, column=0, padx=10, pady=10)
    e1.grid(row=0, column=2, padx=10, pady=10)
    label2.grid(row=1, column=0, padx=10, pady=10)
    e2.grid(row=1, column=2, padx=10, pady=10)
    b.grid(row=3, column=1, padx=10, pady=10)
    w.mainloop()


def clickb3():
    w = customtkinter.CTkToplevel(root)
    w.wm_transient(root) #Makes w appear on top of main window
    w.wm_title("Search Contacts")
    label1 = customtkinter.CTkLabel(w, text="Enter the name of the person\nwhose number is to be found")
    e1 = customtkinter.CTkEntry(w)

    def success():
        if search(e1.get()) == False:
            messagebox.showinfo("Error", f"{e1.get()} does not exist in the directory.")
        else:
            messagebox.showinfo("Message", f"The phone number of the given person is {search(e1.get())}")
            w.destroy()
    b = customtkinter.CTkButton(w, text="SUBMIT", command=success)
    label1.grid(row=0, column=0, padx=10, pady=10)
    e1.grid(row=0, column=2, padx=10, pady=10)
    b.grid(row=1, column=1, padx=10, pady=10)
    w.mainloop()


def clickb4():
    w = customtkinter.CTkToplevel(root)
    w.wm_transient(root) #Makes w appear on top of main window
    w.wm_title("Delete Contacts")
    label1 = customtkinter.CTkLabel(w, text="Enter the name of the person\nwho is to be deleted from the directory")
    e1 = customtkinter.CTkEntry(w)

    def success():
        if delete(e1.get()) == False:
            messagebox.showinfo("Error", f"{e1.get()} does not exist in the directory.")
            w.destroy()
        else:
            messagebox.showinfo("Message", "SUCCESSFULLY DELETED!")
            w.destroy()
    b = customtkinter.CTkButton(w, text="SUBMIT", command=success)
    label1.grid(row=0, column=0, padx=10, pady=10)
    e1.grid(row=0, column=2, padx=10, pady=10)
    b.grid(row=1, column=1, padx=10, pady=10)
    w.mainloop()


def clickb5():
    w = customtkinter.CTkToplevel(root)
    w.wm_transient(root) #Makes w appear on top of main window
    w.wm_title("Clear All Contacts")
    w.geometry("300x150")
    label1 = customtkinter.CTkLabel(w, text="Are you sure you want to clear\nout all data from the directory?",font=("Trebuchet MS", 15))
    label1.pack(side=TOP)

    def success():
        if wipe() == True:
            messagebox.showinfo("Message", "Phonebook successfully cleared")
        if wipe() == False:
            messagebox.showinfo("Error", "Phonebook is already empty")
            w.destroy()
    b1 = customtkinter.CTkButton(w, text="YES", command=success)
    b2 = customtkinter.CTkButton(w, text="NO", command=w.destroy)
    b1.pack(padx=15, pady=10)
    b2.pack(padx=15, pady=10)
    w.mainloop()


def clickb6():
    w = customtkinter.CTkToplevel(root)
    w.wm_title("Display Contacts")
    w.geometry("350x350")
    w.minsize(350, 350)
    w.wm_transient(root) #Makes w appear on top of main window
    w.wm_title()
    f=customtkinter.CTkScrollableFrame(w,width=350,height=350)
    f.pack()
    if display()==False:
        w.destroy()
        messagebox.showinfo("Error","You have no contacts. Please add new ones")
    else:
        label1 = customtkinter.CTkLabel(f, text="Name               Number",font=("Trebuchet MS", 20))
        label1.pack(pady=10)
        for i in display():
                        label = customtkinter.CTkLabel(f, text=f"{i[0]}                      {i[1]}",font=("Arial", 15))
                        label.pack(padx=10,pady=10)
    w.mainloop()
        
def clickb7():
    customtkinter.set_appearance_mode("light")


def clickb8():
    customtkinter.set_appearance_mode("dark")


b1 = customtkinter.CTkButton(root, text="Add Contacts", font=("Trebuchet MS", 15), command=clickb1)
b1.pack(side=TOP, padx=5, pady=15)
b2 = customtkinter.CTkButton(root, text="Update Contacts", font=("Trebuchet MS", 15), command=clickb2)
b2.pack(side=TOP, padx=5, pady=15)
b3 = customtkinter.CTkButton(root, text="Search Contacts", font=("Trebuchet MS", 15), command=clickb3)
b3.pack(side=TOP, padx=5, pady=15)
b4 = customtkinter.CTkButton(root, text="Delete Contacts", font=("Trebuchet MS", 15), command=clickb4, height=30, width=40)
b4.pack(side=TOP, padx=5, pady=15)
b5 = customtkinter.CTkButton(root, text="Clear all contacts ", font=("Trebuchet MS", 15), command=clickb5, height=30,width=20)
b5.pack(side=TOP, pady=15)
b6 = customtkinter.CTkButton(root, text="Display Contacts", command=clickb6, font=("Trebuchet MS", 15), height=30,width=20)
b6.pack(pady=15)
b7 = customtkinter.CTkButton(root, text="Light mode", command=clickb7, height=5, width=10)
b7.pack(side=LEFT, pady=5)
b8 = customtkinter.CTkButton(root, text="Dark mode", command=clickb8, height=5, width=10)
b8.pack(side=RIGHT, pady=5)
root.mainloop()    
