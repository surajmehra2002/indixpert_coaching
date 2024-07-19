
# extend() for list == update() for set = for merging 
# append() for list == add() for set = for add new single element
    
    


# syntax of merging of list 
# studentlist1 = ["suraj", "vimal", "tnuja"]
# studentlist2 = ["nisha", "mazda"]
# studentlist1.extend(studentlist2)
# print(studentlist1)

# syntax of merging of set
# studentlist1 = {"suraj", "vimal", "tnuja"}
# studentlist2 = {"nisha", "mazda"}
# studentlist1.update(studentlist2)
# print(studentlist1)


# studentlist1 = ["suraj", "vimal", "tnuja"]
# studentlist1.append("neeraj")
# print(studentlist1)

# studentlist1 = {"suraj", "vimal", "tnuja"}
# studentlist1.add("neeraj")
# print(studentlist1)

# studentlist1 = ["suraj", "vimal", "tanuja","gaurav"]
# studentlist1.remove("vimal")
# print(studentlist1)

# studentlist1 = ["suraj", "vimal", "tnuja"]
# studentlist2 = studentlist1.copy()
# print(studentlist2)

# studentlist1 = ["suraj", "vimal", "tnuja"]
# studentlist2 = studentlist1.copy()
# studentlist1.clear()

# print(studentlist2)
# print(studentlist1)

# list1 = [1,2,3,4,5,1]
# list2 = [1,2,8,9,10]

# list_new1 = list(set(list1))
# list_new2 = list(set(list2))

 
n = int(input("Enter the no of element in list: "))

list1 = []
list2 = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    list1.append(num)

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    list2.append(num)

print("two list after input: ")
print(list1)
print(list2)
    
list_new1 = []
list_new2 = []

for element in list1:
    if element not in list_new1:
        list_new1.append(element)
    
for element in list2:
    if element not in list_new2:
        list_new2.append(element)

print("common element in both list: ")
for element in list_new1:
    if element in list_new2:
        print(element, end=' ')


