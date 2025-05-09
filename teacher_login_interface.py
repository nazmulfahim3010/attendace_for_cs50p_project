import sys
from validate_email_address import validate_email # type: ignore
def main():
    teacher()


def teacher():
    dec=input("you need to create?(yes/no) ").lower()
    if "no" in dec:
        create_ac()
    elif "yes" in dec:
        match_ac()
    else:
        sys.exit("Invalid answer please check and restart the system")
    ...

    
def create_ac(): #no
    name=input("Name: ")
    
    email_pass=verfication_of_data()
    email=email_pass[0] # type: ignore
    password=email_pass[1] # type: ignore

    teacher_data={
        "name":[],
        "email":[],
        "password":[]
    }

    teacher_data["name"].append(name)
    teacher_data["email"].append(email)
    teacher_data["password"].append(password)

    print(teacher_data)
    ...
def match_ac():
    print("working match")
    ...


def verfication_of_data():
    
    while True:
        email=input("email:")
        if validate_email(email):
            is_right_mail=True
            break#email verification    
            ...
        else:
            print("your email is not valid")
            
    while True:
        password1=input("password: ")
        password2=input("re type your password: ")        

        if password1==password2:
            password=password1
            is_right_pass=True
            break
        else:
            print("password Invlid")

    if is_right_mail and is_right_pass:
        return email,password



    ...
if __name__=="__main__":
    main()



'''
in this file will make sure that files are accessed by teachers only , so that any one can not
touch the file csv , they need to login fisrt to acces those file
'''
