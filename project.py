from student_data_input_sys import data_input
from teacher_login_interface import teacher
from attendance_one_by_one import read_,see_total_attendance
import sys

def main():
    if teacher():
        menu()
    else:
        sys.exit("something wrong")
    ...

def menu():
    ans= menu_dec()
    if ans=='4':
        data_input()
        menu()
    elif ans=='1':
        read_()
        menu()
    elif ans=='3':
        see_total_attendance()
        menu()


    
    ...
def menu_dec():
    print("features:\n1.create a new student file\n2.attendance \n3.total attendeance" \
        "\n")
    ans=input()
    return ans


if __name__=="__main__":
    main()