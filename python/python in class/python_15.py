# nested dictionary and utilisation in python 

students = {
    "user_1": {
        "name": "suraj",
        "class": "BCA",
        "location": "bageshwar"
    },
    "user_2": {
        "name": "vimal",
        "class": "BSC",
        "location": {"home":"bageshwar", "job":"noida"}
    }
}

# for change
# students["user_2"]["location"]={"work":"jarti","trevel":"kapkot"}

# for add new element
# students["user_2"]["location"].update({"work":"jarti","trevel":"kapkot"})




print(students["user_2"]["location"])

