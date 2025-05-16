from teacher_login_interface import collect_saved_data
import csv
import pandas as pd

def main():
    read_()
    see_total_attendance()
    ...
def read_():    

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

    df=pd.read_csv("student sheet.csv")
    df['attendance']=attendance
    df.to_csv('student sheet.csv',index=False)
    ...


def see_total_attendance():
    print("id-> ***-***-000 \n indicates this your total working day")
    df=pd.read_csv("student sheet.csv")
    
    print(df)
    ...



if __name__=="__main__":
    main()