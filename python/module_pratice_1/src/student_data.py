from hitech import hitech_student
from vots import vots_student

print("Task: 1  Hitech Student List")
print("Task: 2  vots Student List")
choise = input("Enter choise no: ")

if choise == "1":
    for student in hitech_student.students():
        print(student)

elif choise == "2":
    for student in vots_student.students():
        print(student)

else:
    print("Enter Valid Task")