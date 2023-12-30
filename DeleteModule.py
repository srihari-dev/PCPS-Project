#Module 3
def delete(x):
    import os
    import csv
    if os.path.exists("Phonebook.csv"):
                                       file=open("Phonebook.csv","r")
    else:
                 return False
    r=csv.reader(file)
    l=[]
    found=0
    for i in r:
        if len(i)==2:
              if i[0]!=x:
                       l.append(i)
              else:
                       found=1
    if found==0:
        return False
    file.close()
    file=open("Phonebook.csv","w") 
    w=csv.writer(file)
    for i in l:
        w.writerow(i)
    file.close()
    return True
    
