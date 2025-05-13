from teacher_login_interface import collect_saved_data
import csv
def main():
    
    ...
def read_():
    
    attendance=[]
    
    with open('student sheet.csv', mode='r') as file:  
        reader = csv.DictReader(file)
        for row in reader:
            print(row['id'])
            x=input(f" ")
            attendance.append(x)
            
    


if __name__=="__main__":
    main()