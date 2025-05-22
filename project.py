from student_data_input_sys import data_input
from teacher_login_interface import teacher
from attendance_one_by_one import read_,see_total_attendance
from add_file_name import build_file
from project_msg import figlet_msg,cowsay_msg_ghost
import sys

def main():
    if teacher():
        menu()
    else:
        sys.exit("something wrong")


def menu():
    try:
        ans= menu_dec()
        if ans=='1':
            data_input()
            menu()
        elif ans=='2':
            file_name=build_file()
            read_(file_name)
            menu()
        elif ans=='3':
            file_name=build_file()
            see_total_attendance(file_name)
            menu()
        else:
            print(cowsay_msg_ghost("wrong command"))
            menu()
    except(TypeError):
        menu()




    ...
def menu_dec():
    print("features:\n1.create a new student file\n2.attendance \n3.total attendeance" \
        "\n")
    ans=input()
    return ans


if __name__=="__main__":
    main()
