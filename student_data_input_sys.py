def main():
    data_input()


def data_input():
    data={
        "id":[],
        "attendence":[]

    }
    student_number=int(input("how many students you want to enter: "))
    student_id="242-234-"#user input
    for s in range(student_number):
        
        data["id"].append(f"{student_id}{s+1:03}")
        
        ...
    print(*data["id"])
if __name__=="__main__":
    main()