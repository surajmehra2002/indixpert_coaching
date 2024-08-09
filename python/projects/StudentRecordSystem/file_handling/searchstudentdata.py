import os, json

def Search_students(JSON_file):
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







def address_students(JSON_file):
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
                print("Student not found with this address!")
    else:
        print("No student data found! Register first..\n")



def id_students(JSON_file):
    if os.path.exists(JSON_file):
        id = int(input("Enter user id: "))
        found = False
        with open(JSON_file, "r") as file:
            data = json.load(file)
            for student in data:
                if student['id']==id:
                    print(json.dumps(student))
                    found = True
                    
            if not found:
                print("Student not found with this ID No!")
    else:
        print("No student data found! Register first..\n")