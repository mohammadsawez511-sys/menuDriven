import os
import csv
fields = ["id","name","fassion","education"]
def create_file(file_name):
    if os.path.exists(file_name):
        print("file already exit")
    else:
        with open(file_name,"w")as f:
            csvWriter = csv.DictWriter(f,fieldnames=fields)
            csvWriter.writeheader()
            print("file is created ")
            f.close()    

def display_data(file_name):
    os.path.exists(file_name)
    with open(file_name,"r",newline="")as f:
        csvReader = csv.DictReader(f)
        for r in csvReader:
            print(r)

def  backup_file(file_name):
    if os.path.exists(file_name):
        with open(file_name,"r")as f:
            data = f.read()
        with open("backup_"+file_name,"w")as f:
            f.write(data)
        print("backup is created ")
    else:
        print("file do not exit ")            

def delete_file(file_name):
    os.remove(file_name)
    print("file is deleted")

def check_record(file_name):
    id = (input("enter search id :"))
    found = False
    with open (file_name,"r",newline="")as f :
        csvReader = csv.DictReader(f)
        for i in csvReader:
            if i["id"]==id:
                print(i)
                found = True
    if       found == False:
                print("record not ")    

print('''write a menu driven application by using python following operation by using 
1:to create a file with name "xyz.csv"
2:to display all data from the csv file 
3:to backup
4:to delete the backup file 
5:to check if a record is present in the file or not 
6:to exit from the application''')


s = int(input("enter your choise : "))
if s == 1:
    create_file(input("enter file name :"))
elif s==2:
    display_data(input("enter file name :"))
elif s==3:
    backup_file(input("enter file name :"))
elif s==4:
    delete_file(input("enter file name :")) 
elif s==5:
    check_record(input("enter file name :"))
elif s==6:
    print("exit application")
else:
    pass           

