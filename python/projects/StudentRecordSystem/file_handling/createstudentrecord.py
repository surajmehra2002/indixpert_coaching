import os, json


def percentage():
    percent = int(input("Enter percentage: "))
    if percent>=0 and percent<=100:
        return percent
    else:
        print("Please Enter percentage between (0--100)")
        return percentage()
        

def student_qualification():
    qualifications = []
    print("Please enter qualifications..\n")
    while True:
        qualification = {}
        qualification["qualificationname"] = input("Enter Qualification name: ")
        qualification["passingyear"] = int(input("Enter passing year: "))
        qualification["percentage"] = percentage()
        qualifications.append(qualification)
        print("\nExit for --0")
        print("More for --1")
        end = int(input("Please press 0 and 1: "))
        if end == 0:
            break
        if end == 1:
            continue
        else:
            print("Invalid Option! Please press 0 and 1")        
    return qualifications


# def uniqe_id():
#     id = 
#     # print(JSON_file)
#     return id


def user_input_data():
    user_dict = {}
    user_dict["id"] = int(input("\nPlease enter student ID: "))
    user_dict["Name"] = input("Please enter student Name: ")
    user_dict["Address"] = input("Please enter student Address: ")
    user_dict["Age"] = int(input("Please enter student Age: "))
    user_dict["Number"] = int(input("Please enter student Number: "))    
    user_dict["Qualification"] = student_qualification()
    return user_dict

def Student_registration(JSON_file):
    if os.path.exists(JSON_file):
        with open(JSON_file,"r") as file:
            list_data = json.load(file)
    
    else:
        list_data = []
    
    list_data.append(user_input_data())

    with open(JSON_file, "w") as file:
        file.write(json.dumps(list_data))
        print("\nData saved Successfully !\n")

