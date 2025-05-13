import csv
from project_msg import cowsay_msg_tux
from project import menu

def main():
    data_input()


def data_input():
    data={
        "id":[],
        "att":[]

    }
    student_number=int(input("how many students you want to enter: "))
    student_id="242-234-"#user input
    for s in range(student_number):
        
        data["id"].append(f"{student_id}{s+1:03}")
        write_id_in_csv(**data)
    
    return
        
    ...
def write_id_in_csv(**data):
    

    with open("student sheet.csv",'w',newline='') as file:
        header=['id','attandance']

        sheet=csv.DictWriter(file,fieldnames=header)
        

        sheet.writeheader()
        for i in range(len(data['id'])):
            sheet_row={
                "id":data['id'][i],
            }

            sheet.writerow(sheet_row)
    print(cowsay_msg_tux("student file has created"))

        
'''
in this page i have taken the user input to put create a csv file named student heet. the data i have passed is easy to create 
a normal sequantial ids according to batch and dept code like 242-134-024;

my next featuer will be i will remove those student who leave the batch and another function to add student 
'''
        

        

    
if __name__=="__main__":
    main()