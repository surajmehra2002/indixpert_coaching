# import numpy as np


# Num_array = []

# n= int(input("How many numbers you want's to add.: "))
# print(f"Enter {n} number's: ")
# for i in range(n):
#         num = int(input())
#         Num_array.append(num)
# print("your array..")
# # Num_array = np.array(Num_array)
# print(Num_array)

# # print("after adding 5")
# # New_array = []
# # for item in Num_array:    
# #     New_array.append(item+5)    
# # print(np.array(New_array))    

# print("after sorting...")
# New_array = []
# # for item in Num_array:    
# #     New_array.append(item+5)    

# New_array1 = New_array.sort()
# print(New_array1)





# import numpy as np

# x = int(input("please enter  numbers how many you want  "))

# print("Please enter numbers:")
# numbers = []
# for i in range(x):
#         num = int(input())
#         numbers.append(num)
        

# # numbers = np.array(numbers)
# print("Array is: \n",numbers )
# print("After add 5: ")
# new_array = []
# for item in numbers:
#         if item<0:
#                 item = 0
#                 new_array.append(item)
#         else:                
#             new_item = item+5
#             new_array.append(new_item)

# new_array1=np.sort(new_array)
# print( new_array1) 

print("*********** [ find number + and -]**********")
import numpy as np

n = int(input("please enter any number, as may as you need:= "))
print("Please enter numbers:")

numbers = []
for i in range(n):
    while True:
        try:
            num = float(input())
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

numbers = np.array(numbers)
numbers += 5
numbers[numbers<0]=0
numbers = np.sort(numbers)
print("Add 5:", numbers)

