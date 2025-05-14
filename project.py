from student_data_input_sys import data_input
from teacher_login_interface import teacher
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

    
    ...
def menu_dec():
    print("features:\n1. attendance \n2.marks input\n3.total attendeance" \
        "\n4.create student attendance file\n")
    ans=input()
    return ans


if __name__=="__main__":
    main()