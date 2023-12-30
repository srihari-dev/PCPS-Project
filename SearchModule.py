# Module 4
def search(x):
    import csv
    import os
    if os.path.exists("Phonebook.csv"):
        file=open("Phonebook.csv","r")
        r=csv.reader(file)
        y=0
        for i in r:
             if len(i)==2:
                     if i[0]== x:
                           y=i[1]
                           break
        if y==0:
           file.close()
           return False
        else:
          file.close()
          return y
    else:
        return False

