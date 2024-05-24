# Username - admin, Password - password

import os
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from prettytable import PrettyTable

# Set TK_SILENCE_DEPRECATION to suppress the warning
os.environ['TK_SILENCE_DEPRECATION'] = '1'

login = Tk()
login.title("Login")
login.geometry("500x500")
login.configure(bg='white')
#login.attributes('-fullscreen', True)

buttonFont = font.Font(family='Arial', size=9, weight='bold')
labelFont = font.Font(family='Arial', size=8, weight='bold')


# Create a function to validate the username and password
def validate_login():
  username = username_entry.get()
  password = password_entry.get()

  # Check if the username and password are correct
  if username == "admin" and password == "password":
    # Close the login window
    login.destroy()
  else:
    # Show an error message and clear the password field
    messagebox.showerror("Error", "Invalid username or password")
    password_entry.delete(0, END)


# Create the login window widgets
username_label = Label(login, text="Username", bg='white')
username_label['font'] = labelFont
username_label.pack()
username_entry = Entry(login)
username_entry.pack()

password_label = Label(login, text="Password", bg='white')
password_label['font'] = labelFont
password_label.pack()
password_entry = Entry(login, show="*")
password_entry.pack()

login_button = Button(login,
                      text="Login",
                      bg='lightcoral',
                      fg='#ffffff',
                      command=validate_login)
login_button['font'] = buttonFont
login_button.pack()

# Start the main loop for the login window
login.mainloop()

# Create the contact management application window
root = Tk()
root.title("Contact Management")
root.geometry("500x400")
root.configure(bg='white')

buttonFont = font.Font(family='Arial', size=9, weight='bold')
lableFont = font.Font(family='Arial', size=8, weight='bold')


# Create a function to connect to the database
def connect():
  """
  Connects to the contact database and creates a contacts table if it     does not exist.
  """
  conn = sqlite3.connect("contacts.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT
        )
    """)
  conn.commit()
  conn.close()


# Create a function to display a message box
def show_message_box(title, message):
  """
  Parameters:
  title(str): Title of message box.
  message(str): Message that is displayed in the message box.
  """
  messagebox.showinfo(title, message)


# Create a function to add a new contact
def add_contact():
  """
  Adds a new contact to the contact database using input values in the    entry fields. There is also a success box when completed, clears the     inputs field.
  """
  # Get input from the user
  first_name = first_name_entry.get()
  last_name = last_name_entry.get()
  email = email_entry.get()
  phone = phone_entry.get()

  # Connect to the database
  conn = sqlite3.connect("contacts.db")
  cursor = conn.cursor()

  # Insert the new contact into the database
  cursor.execute(
    """
        INSERT INTO contacts (first_name, last_name, email, phone)
        VALUES (?, ?, ?, ?)
        """, (first_name, last_name, email, phone))

  conn.commit()
  conn.close()

  # Show a success message
  show_message_box("Success", "Contact added successfully")

  # Clear the input fields
  first_name_entry.delete(0, END)
  last_name_entry.delete(0, END)
  email_entry.delete(0, END)
  phone_entry.delete(0, END)


# Create a function to view all contacts
def view_contacts():
  """
  Retrieves all the contacts from the contact database and displays in the message box.
  """
  # Connect to the database
  conn = sqlite3.connect("contacts.db")
  cursor = conn.cursor()

  # Get all contacts from the database
  cursor.execute("SELECT * FROM contacts")
  rows = cursor.fetchall()

  # Close the database connection
  conn.close()

  # Create a pretty table to display the contacts
  table = PrettyTable()
  table.field_names = ["ID", "First Name", "Last Name", "Email", "Phone"]

  # Add rows to the table
  for row in rows:
    table.add_row(row)

  # Display the table in a message box
  show_message_box("Contacts", str(table))


# Create a function to delete a contact
# Create a function to delete a contact
def delete_contact():
  """
    Deletes a contact from the contact database based on the selected ID.
    """

  def delete():
    # Get the ID of the contact to be deleted
    contact_id = id_entry.get()

    # Connect to the database
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    # Delete the contact from the database
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id, ))

    conn.commit()
    conn.close()

    # Destroy the popup window
    popup.destroy()

    # Show a success message
    show_message_box("Success", "Contact deleted successfully")

  # Create the popup window
  popup = Toplevel(root)
  popup.title("Delete Contact")
  popup.geometry("300x200")
  popup.configure(bg='white')

  # Create the "Enter ID to delete" label and pack it onto the popup window
  delete_label = Label(popup, text="Enter ID to delete:", bg='white')
  delete_label['font'] = labelFont
  delete_label.pack()

  # Create the ID entry field and pack it onto the popup window
  id_entry = Entry(popup)
  id_entry.pack()

  # Create the delete button and pack it onto the popup window
  delete_button = Button(popup,
                         text="Delete",
                         bg='lightcoral',
                         fg='#ffffff',
                         command=delete)
  delete_button['font'] = buttonFont
  delete_button.pack()

  # Center the popup window on the screen
  popup.update_idletasks()
  width = popup.winfo_width()
  height = popup.winfo_height()
  x = (popup.winfo_screenwidth() // 2) - (width // 2)
  y = (popup.winfo_screenheight() // 2) - (height // 2)
  popup.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def edit_contacts():
  """
    Allows the user to edit an existing contact based on their ID
    """
  # Create a pop-up window to get the contact details
  edit_window = Toplevel()
  edit_window.title("Edit Contact")
  edit_window.geometry("300x250")
  edit_window.configure(bg='white')

  id_label = Label(edit_window, text="ID:", bg='white')
  id_label['font'] = labelFont
  id_label.pack()
  id_entry = Entry(edit_window)
  id_entry.pack()

  first_name_label = Label(edit_window, text="First Name:", bg='white')
  first_name_label['font'] = labelFont
  first_name_label.pack()
  first_name_entry = Entry(edit_window)
  first_name_entry.pack()

  last_name_label = Label(edit_window, text="Last Name:", bg='white')
  last_name_label['font'] = labelFont
  last_name_label.pack()
  last_name_entry = Entry(edit_window)
  last_name_entry.pack()

  email_label = Label(edit_window, text="Email:", bg='white')
  email_label['font'] = labelFont
  email_label.pack()
  email_entry = Entry(edit_window)
  email_entry.pack()

  phone_label = Label(edit_window, text="Phone:", bg='white')
  phone_label['font'] = labelFont
  phone_label.pack()
  phone_entry = Entry(edit_window)
  phone_entry.pack()

  def update_contact():
    # Get the values entered by the user
    id_val = id_entry.get()
    first_name_val = first_name_entry.get()
    last_name_val = last_name_entry.get()
    email_val = email_entry.get()
    phone_val = phone_entry.get()

    # Connect to the database
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute(
      """
                UPDATE contacts SET 
                    first_name = ?,
                    last_name = ?,
                    email = ?,
                    phone = ?
                WHERE id = ?
            """, (first_name_val, last_name_val, email_val, phone_val, id_val))

    conn.commit()
    conn.close()
    show_message_box("Success", "Contact updated successfully")
    edit_window.destroy()

  # Create a button to update the contact
  update_button = Button(edit_window,
                         text="Update Contact",
                         bg='lightcoral',
                         fg='#ffffff',
                         command=update_contact)
  update_button['font'] = buttonFont
  update_button.pack()

  edit_window.mainloop()


# Create labels and entry fields for input
first_name_label = Label(root, text="First Name", bg='white')
first_name_label['font'] = lableFont
first_name_label.pack()
first_name_entry = Entry(root)
first_name_entry.pack()

last_name_label = Label(root, text="Last Name", bg='white')
last_name_label['font'] = lableFont
last_name_label.pack()
last_name_entry = Entry(root)
last_name_entry.pack()

email_label = Label(root, text="Email", bg='white')
email_label['font'] = lableFont
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

phone_label = Label(root, text="Phone", bg='white')
phone_label['font'] = lableFont
phone_label.pack()
phone_entry = Entry(root)
phone_entry.pack()

# Create buttons to manage contacts
add_button = Button(root,
                    text="Add Contact",
                    bg='lightcoral',
                    fg='#ffffff',
                    command=add_contact)
add_button['font'] = buttonFont
add_button.pack()

view_button = Button(root,
                     text="View Contacts",
                     bg='lightcoral',
                     fg='#ffffff',
                     command=view_contacts)
view_button['font'] = buttonFont
view_button.pack()

edit_button = Button(root,
                     text="Edit Contacts",
                     bg='lightcoral',
                     fg='#ffffff',
                     command=edit_contacts)
edit_button['font'] = buttonFont
edit_button.pack()

delete_button = Button(root,
                       text="Delete Contact",
                       bg='lightcoral',
                       fg='#ffffff',
                       command=delete_contact)
delete_button['font'] = buttonFont
delete_button.pack()

# Call the connect function to setup the database
connect()

# Run the main loop
root.mainloop()