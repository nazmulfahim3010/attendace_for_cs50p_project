def main():
    
    build_file()

def build_file():
    batch_id={
        "1st":"212-134-",
        "2nd":"221-134-",
        "3rd":"222-134-",
        "4th":"231-134-",
        "5th":"232-134-",
        "6th":"241-134-",
        "7th":"242-134-"
    }

    student_batch=input("student batch number? ")
    student_id=batch_id[student_batch]
    sheet_name=f"{student_id} {student_batch} sheet.csv"
    
    return sheet_name


if __name__=="__main__":
    main()