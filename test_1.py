import csv
from teacher_login_interface import verfication_of_data
import pyfiglet#type:ignore
import datetime
import sys
def main():
    match_ac()
    

def match_ac():
    i=0
    while i<3:
    
        email_and_pass=verfication_of_data()
        email=email_and_pass[0]#type:ignore
        password=email_and_pass[1]#type:ignore
        #email="fahm@gmail.com"
        #password="1234"

        with open("teacher_data.csv",'r') as file:
            lines=csv.DictReader(file)
            for line in lines:
                
                if email in line['email'] and password in line['password']:
                    welcome()
                    return    
            
            print("user email and password is wrong")    
        i+=1
        
def welcome():
    msg=pyfiglet.figlet_format("wellcome")
    print(msg)
    date=datetime.datetime.now()
    print(f"date:{date.day}-{date.month}-{date.year}\ntime:{date.hour}:{date.minute}")


if __name__=="__main__":
    main() 