#Module 6
def wipe():
    import csv
    import os
    file="Phonebook.csv"
    if os.path.exists(file):
                 os.remove(file)
                 return True
                
  
