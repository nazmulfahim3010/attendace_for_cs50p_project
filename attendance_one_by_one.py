from teacher_login_interface import collect_saved_data
import csv
import pandas as pd
from add_file_name import build_file

def main():
    file_name=build_file()
    read_(file_name)
    see_total_attendance(file_name)
    ...
def read_(file_name): 
       

    with open(file_name,"r") as file:
        lines=csv.DictReader(file)
        attendance=[]
        id_s=[]

        for line in lines:

            attendance.append(int(line['attendance']))
            id_s.append(line["id"])

    for i in range(len(attendance)):
        is_bool=True
        
        while is_bool:
            if i==0:
                attendance[i]+=1
                break
            x=input(f"{id_s[i]} ")
                
            if x=="p":
                attendance[i]+=1
                is_bool=False
            elif x=='a':
                attendance[i]+=0
                is_bool=False
            else:
                print("you put wrong command")
                is_bool=True
                
                ...    

    df=pd.read_csv(file_name)
    df['attendance']=attendance
    df.to_csv(file_name,index=False)
    ...


def see_total_attendance(file_name):
    print("id-> ***-***-000 \n indicates this your total working day")
    df=pd.read_csv(file_name)
    
    print(df)
    ...



if __name__=="__main__":
    main()