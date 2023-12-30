def display():
    import csv
    import os
    if not os.path.exists("Phonebook.csv"):
        return False
    with open("Phonebook.csv", "r") as file:
        r = csv.reader(file)
        entries = [i for i in r if len(i) == 2]
    if not entries:
        return False
    return entries

