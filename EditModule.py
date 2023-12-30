# Module 2
def edit(x,y):
    import os
    import csv
    if len(y)!=10 or not y.isdigit():
                                       return "invalid"
    if os.path.exists("Phonebook.csv"):
                                       file=open("Phonebook.csv","r")
    else:
                 return False
    r=csv.reader(file)
    l=[]
    found=0
    for i in r:
        if len(i)==2:
              if i[0]==x:
                       l.append([x,y])
                       found=1
              else:
                       l.append(i)
    if found==0:
        return False
    file.close()
    file=open("Phonebook.csv","w") 
    w=csv.writer(file)
    for i in l:
        w.writerow(i)
    file.close()
    return True
