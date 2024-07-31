import os

path = 'S:/CODE/user_choise_files/'

def no_of_files(directry):
    elements = os.listdir(directry)   
    all_files = sum(1 for element in elements if os.path.isfile(os.path.join(path, element)))    
    return all_files


total_files = no_of_files(path)


n = int(input("Enter no of file do you want to create: "))

for i in range (n):

    with open(path + f"{total_files+1}.txt", "w" ) as file:
        file.write(f"the file no is {total_files+1}")
    total_files+=1
print("successfully created")























#         num_files = int(input("Enter a number between 1 and 5: "))
#         if 1 <= num_files <= 5:
#             break
#         else:
#             print("The number must be between 1 and 5.")
# for i in range(1, num_files + 1):


# import datetime
# today = datetime.datetime.now()
# # print(today+datetime.timedelta(days=5))
# print(today+datetime.add_days(5))