import csv
from project_msg import cowsay_msg_tux,figlet_msg
from add_file_name import build_file
from tabulate import tabulate #type:ignore


def main():
    data_input()


def data_input():
    data={
        "id":[],
        "att":[],
        

    }
    batch_id={
        "1st":"212-134-",
        "2nd":"221-134-",
        "3rd":"222-134-",
        "4th":"231-134-",
        "5th":"232-134-",
        "6th":"241-134-",
        "7th":"242-134-"
    }

    data_for_batch = [
    {"BATCH": "1st", "BATCH ID": "212-134-***"},
    {"BATCH": "2nd", "BATCH ID": "221-134-***"},
    {"BATCH": "3rd", "BATCH ID": "222-134-***"},
    {"BATCH": "4th", "BATCH ID": "231-134-***"},
    {"BATCH": "5th", "BATCH ID": "232-134-***"},
    {"BATCH": "6th", "BATCH ID": "241-134-***"},
    {"BATCH": "7th", "BATCH ID": "242-134-***"},
    {"BATCH": "8th", "BATCH ID": "251-134-***"},
    {"BATCH": "9th", "BATCH ID": "252-134-***"}
]

    print(tabulate(data_for_batch, headers="keys", tablefmt="fancy_grid"))

    student_batch=input("Your student batch number? ")
    student_id=batch_id[student_batch]
    sheet_name=f"{student_id} {student_batch} sheet.csv"
    
    
    student_number=int(input("how many students you want to enter: "))


    
    for s in range(student_number+1):
         
        data["id"].append(f"{student_id}{s:03}")
        data["att"].append(0)
        data["file_name"]=sheet_name # type: ignore
        write_id_in_csv(**data)

    print(cowsay_msg_tux("student file has created"))
    
    return
        
    ...
def write_id_in_csv(**data):
    need_sheet_name=True
    file_name=data["file_name"]
    


    with open(file_name,'w',newline='') as file:
        header=['id','attendance']

        sheet=csv.DictWriter(file,fieldnames=header)
        

        sheet.writeheader()
        for i in range(len(data['id'])):
            sheet_row={
                "id":data['id'][i],
                "attendance":data["att"][i]
            }

            sheet.writerow(sheet_row)

        
'''
in this page i have taken the user input to put create a csv file named student heet. the data i have passed is easy to create 
a normal sequantial ids according to batch and dept code like 242-134-024;

my next featuer will be i will remove those student who leave the batch and another function to add student 
'''


    
if __name__=="__main__":
    main()