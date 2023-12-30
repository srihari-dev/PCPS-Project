#Module 1
def add(x,y):
    import csv
    import os
    if len(y)!=10 or not y.isdigit():
                                       return False
    def check():
        if os.path.exists("Phonebook.csv"):
            f=open("Phonebook.csv","r+")
            r=csv.reader(f)
            for i in r:
                if len(i)==2:
                      if i[0]==x or i[1]==y:
                             f.close()
                             return True
            f.close()
        return False
    if check()==True:
                   return "alreadyexists"
    elif check()==False:
                   file=open("Phonebook.csv","a+")
                   w=csv.writer(file)
                   w.writerow([x,y])
                   file.close()
    return True
