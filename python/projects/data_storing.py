import os, json

JSON_file = r"S:\indixpert_coaching\python\data_storing_files/user_data.json"




def user_input_data():
    user_dict = {}
    user_dict["id"] = int(input("Please enter student ID: "))
    user_dict["Name"] = input("Please enter student Name: ")
    user_dict["Address"] = input("Please enter student Address: ")
    user_dict["Age"] = int(input("Please enter student Age: "))
    user_dict["Number"] = int(input("Please enter student Number: "))    
    return user_dict



def Student_registration():
    if os.path.exists(JSON_file):
        with open(JSON_file,"r") as file:
            list_data = json.load(file)
    
    else:
        list_data = []
    
    list_data.append(user_input_data())

    with open(JSON_file, "w") as file:
        file.write(json.dumps(list_data))
        print("\nData saved Successfully !\n")




def Saved_students():
    if os.path.exists(JSON_file):
        with open(JSON_file) as file:
            data = json.load(file)
            for student in data:
                print(student)
            # print(file.read())
            # list_data = json.load(file)
            # print(json.dumps(list_data))
    else:
        print("No student data found! Register first..\n")


def Search_students():
    if os.path.exists(JSON_file):
        number = int(input("Enter user mobile no. : "))
        found = False
        with open(JSON_file, "r") as file:
            data = json.load(file)
            for student in data:
                if student['Number']==number:
                    print("Student Found! ")
                    print(json.dumps(student))
                    found = True
                    break
                    
            if not found:
                print("Student not found with this mobile No!")
    else:
        print("No student data found! Register first..\n")


def address_students():
    if os.path.exists(JSON_file):
        address = input("Enter user address: ")
        found = False
        with open(JSON_file, "r") as file:
            data = json.load(file)
            for student in data:
                if student['Address']==address:
                    print(json.dumps(student))
                    found = True
                    
            if not found:
                print("Student not found with this mobile No!")
    else:
        print("No student data found! Register first..\n")




while True:
    print("\nEnter -1 Students registration")
    print("Enter -2 view Students data")
    print("Enter -3 Search Student data with mobile no.")
    print("Enter -4 Search Students with address.")
    print("Enter -0 Exit...")
    choice = input("choice any option: ")
    match choice:
        case '1':
            Student_registration()
        case '2':
            Saved_students()
        case '3':
            Search_students()
        case '4':
            address_students()
        case '0':
            break
        case _:
            print("\nInvalid option! Tri again..")
   













