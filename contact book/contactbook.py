from tkinter import *
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    contact = contact_entry.get()
    gmail = gmail_entry.get()
    
    if name and contact:
        if gmail:
            contact_list.insert(END, f"name: {name}, phno: {contact}, Gmail: {gmail}")
        else:
            contact_list.insert(END, f"name: {name}, phno: {contact}")
        name_entry.delete(0, END)
        contact_entry.delete(0, END)
        gmail_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter both name and contact information.")

def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contact_list.delete(selected_index)
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def clear_contacts():
    contact_list.delete(0, END)

def get_selected_contact(event):
    try:
        selected_index = contact_list.curselection()[0]
        selected_contact = contact_list.get(selected_index)
        if "Gmail: " in selected_contact:
            parts = selected_contact.split(", ")
            name_entry.delete(0, END)
            contact_entry.delete(0, END)
            gmail_entry.delete(0, END)
            name_entry.insert(END, parts[0].replace("Name: ", ""))
            contact_entry.insert(END, parts[2].replace("Phno: ", ""))
            gmail_entry.insert(END, parts[4].replace("Gmail: ", ""))
        else:
            parts = selected_contact.split(", ")
            name_entry.delete(0, END)
            contact_entry.delete(0, END)
            gmail_entry.delete(0, END)
            name_entry.insert(END, parts[0].replace("Name: ", ""))
            contact_entry.insert(END, parts[1].replace("Phno: ", ""))
    except IndexError:
        pass

root = Tk()
root.title("Contact Book")

# Set window size
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Create UI elements
name_label = Label(root, text="Name:", font=("Helvetica", 12, "bold"))  # Make title bold
name_label.pack()
name_entry = Entry(root, width=50)  # Increase width to 50 characters
name_entry.pack()

contact_label = Label(root, text="Contact:", font=("Helvetica", 12, "bold"))  # Make title bold
contact_label.pack()
contact_entry = Entry(root, width=50)  # Increase width to 50 characters
contact_entry.pack()

gmail_label = Label(root, text="Gmail:", font=("Helvetica", 12, "bold"))  # Make title bold
gmail_label.pack()
gmail_entry = Entry(root, width=50)  # Increase width to 50 characters
gmail_entry.pack()

add_button = Button(root, text="Add Contact", command=add_contact)
add_button.pack()

delete_button = Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

clear_button = Button(root, text="Clear Contacts", command=clear_contacts)
clear_button.pack()

contact_list = Listbox(root, width=80, font=("Helvetica", 12), bg="light gray")  # Set background color to light gray
contact_list.pack()

contact_list.bind('<<ListboxSelect>>', get_selected_contact)

root.mainloop()
