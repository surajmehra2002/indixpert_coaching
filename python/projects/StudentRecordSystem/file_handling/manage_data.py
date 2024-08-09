import sys
sys.path.append(r'S:\indixpert_coaching\python\projects\StudentRecordSystem\file_handling')


JSON_file = r"S:\indixpert_coaching\python\data_storing_files/user_data.json"

import createstudentrecord
import displaystudentrecords
import searchstudentdata

def Dashbord():

    while True:
        print("\nEnter -1 Students registration")
        print("Enter -2 view Students data")
        print("Enter -3 Search Student data with mobile no.")
        print("Enter -4 How many students are located with addresses.")
        print("Enter -5 Search Students with id number.")
        print("Enter -0 Exit...")
        choice = input("choice any option: ")
        match choice:
            case '1':
                createstudentrecord.Student_registration(JSON_file)
            case '2':
                displaystudentrecords.Saved_students(JSON_file)
            case '3':
                searchstudentdata.Search_students(JSON_file)
            case '4':
                searchstudentdata.address_students(JSON_file)
            case '5':
                searchstudentdata.id_students(JSON_file)
            case '0':
                break
            case _:
                print("\nInvalid option! Tri again..")
