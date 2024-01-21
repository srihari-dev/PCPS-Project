# Phone Book Application

This is a Python application that creates a simple phone book with basic contact management features.

## Features

Add contacts: Enter a name and a 10-digit phone number to add a new contact.
Update contacts: Modify the phone number of an existing contact.
Search contacts: Find a contact's phone number by searching for their name.
Delete contacts: Remove a contact from the phone book.
View all contacts: Display a list of all contacts with their names and phone numbers.
Clear all contacts: Delete all contacts from the phone book.
Switch between light and dark mode: Change the application's appearance.
## Requirements

Python 3.x
Required modules: tkinter, customtkinter, datetime
Additional modules (must be in the same directory): AddModule.py, EditModule.py, DeleteModule.py, SearchModule.py, DisplayModule.py, WipeModule.py
## Instructions to Run

1) Install the required modules
```bash
pip install tkinter
pip install customtkinter
```
2) Place all the Python files (main script and additional modules) in the same directory.

3) Run the main script:
```bash
python PHONEBOOK APPLICATION.py  
```

## Usage

The application's interface is self-explanatory. Click the buttons to perform the corresponding actions.
Enter names and phone numbers in the provided text fields.
Click "Submit" to confirm actions.

## Additional Notes

The phone book data is not persisted between sessions.
Phone numbers must be 10 digits long.
The application currently does not support duplicate names or phone numbers.
For detailed functionality of each feature, refer to the code itself.


