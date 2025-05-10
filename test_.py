import csv


email_list=[]
with open("teacher_data.csv",mode='r') as file:
    read_=csv.DictReader(file)
    
    for line in read_:
        email_list.append(line['email'])
        
    
print(email_list)
