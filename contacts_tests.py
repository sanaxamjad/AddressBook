#edit_contacts unit test
def test_(self):
  # Test editing an existing contact with valid data
        id_entry = "1"
        first_name_entry = "Jane"
        last_name_entry = "Doe"
        email_entry = "janedoe@example.com"
        phone_entry = "987-654-3210"
        self.assertEqual(edit_contacts(), None)

#view_contacts
def test_(self):
   # Test viewing all contacts
        self.assertEqual(view_contacts(), None)


#add_contacts
def test_(self):
   # Test adding a new contact with valid data
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        email_entry.delete(0, END)
        phone_entry.delete(0, END)
        first_name_entry.insert(0, "John")
        last_name_entry.insert(0, "Doe")
        email_entry.insert(0, "johndoe@example.com")
        phone_entry.insert(0, "123-456-7890")
        self.assertEqual(add_contact(), None)

#validate_login
def test_(self):
   # Test with valid username and password
        self.assertEqual(validate_login(), None)

        # Test with invalid username and password
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        username_entry.insert(0, "invalid_username")
        password_entry.insert(0, "invalid_password")
        self.assertEqual(validate_login(), None)
        
 
#delete_contacts
def test_(self):
  # Test deleting an existing contact with valid data
        id_entry = "1"
        self.assertEqual(delete_contacts(), None)
      
 #connect
def test_(self):
  # Testing to make sure that database is connected
            self.assertEqual(connect(), None)

