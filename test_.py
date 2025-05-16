#give attedance

import pandas as pd
from datetime import date
import csv

with open("student sheet.csv","r") as file:
    lines=csv.DictReader(file)
    attendance=[]
    id_s=[]

    for line in lines:

        attendance.append(int(line['attendance']))
        id_s.append(line["id"])

for i in range(len(attendance)):
    is_bool=True
    
    while is_bool:
        x=input(f"{id_s[i]} ")
        if x=="p":
            attendance[i]+=1
            is_bool=False
        elif x=='a':
            attendance[i]+=0
            is_bool=False
        else:
            is_bool=True
            
            ...    

df=pd.read_csv("student sheet.csv")
df['attendance']=attendance
df.to_csv('student sheet.csv',index=False)
...





