import csv

users_dict = {}
names=[]
emails=[]
passwords=[]

with open('teacher_data.csv', mode='r') as file:  
    reader = csv.DictReader(file)
    for row in reader:
        names.append(row['name'])
        emails.append(row['email'])
        passwords.append(row['password'])


        





'''import csv
data={
        "id":[1,2,3],
        "attendence":["p","a",'p']

    }
rows=zip(data["id"],data["attendence"])
with open("data.csv","w",newline='') as file:
    writer=csv.writer(file)

    writer.writerow(["id","attendence"])
    writer.writerows(rows)
'''