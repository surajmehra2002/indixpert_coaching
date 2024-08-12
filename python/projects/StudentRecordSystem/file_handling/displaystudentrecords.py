import os, json



def all_students(JSON_file):
    with open(JSON_file) as file:
            data = json.load(file)
            print(f"Totle {len(data)} user's are available")
            for student in data:
                print(student)
    
            
    

def toppers(JSON_file):
    
    topper_list = []
    topper = []  
    with open(JSON_file) as file:
        data = json.load(file)
        for student in data:
            no = 0
            for item in student["Qualification"]:
                no = no + item["percentage"]
            topper.append(no)
        topper3 = sorted(topper, reverse=True)[:3] 
        for student in data:
            no = 0
            for item in student["Qualification"]:
                no = no + item["percentage"]
            if no == topper3[0]:
                first = {}
                first["id"] = student["id"]
                first["percent"] = topper3[0]
                topper_list.append(first)
            if no == topper3[1]:
                second = {}
                second["id"] = student["id"]
                second["percent"] = topper3[1]
                topper_list.append(second)
            if no == topper3[2]:
                third = {}
                third["id"] = student["id"]
                third["percent"] = topper3[2]
                topper_list.append(third)
        sorted_students = sorted(topper_list, key=lambda x: x["percent"], reverse=True)      
        print(sorted_students)      
        print("\n All student record in details..\n")      


        detail_topper_list = [None,None,None]
        for student in data:
            no = 0
            
            for item in student["Qualification"]:
                no = no + item["percentage"]
            if no == topper3[0]:
                # this student will first
                detail_topper_list[0] = student
            if no == topper3[1]:
                # this student will second
                detail_topper_list[1] = student
            if no == topper3[2]:
                # this student will third
                detail_topper_list[2] = student

        print(json.dumps(detail_topper_list, indent=2))

                   
    

def Saved_students(JSON_file):
    if os.path.exists(JSON_file):
        print("\npress --1 all Students records")
        print("press --2 Top 3 Student records")
        choise = int(input("Enter your choise: "))
        if choise==1:
            all_students(JSON_file)
        if choise==2:
            toppers(JSON_file)
    else:
        print("No student data found! Register first..\n")   


    

