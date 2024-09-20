# INPUT: 

# 5
# 10 20 30 15 12

# OUTPUT:
# 10 12 15 20 30

# *****************************************************START****************************************************

# n = int(input())

num = input()
# 1 2 3 4 5

str_list = num.split(" ")
# ['1', '2', '3', '4', '5']


# num_list = list(map(int,str_list))
num_list = []
for num in str_list:
    num_list.append(int(num))

num_list.sort()

# print(num_list)

# str_format = " ".join(map(str, num_list))  # [1, 2, 3, 4]  =>  "1 2 3 4"
str_format = ""
for item in num_list:
    str_format = str_format+str(item)+" "


print(str_format)



# print(type(num.split(" ")))
# A = list(map(int, num.split(" ")))
# print(A)

# B = list(set(A))

# print(" ".join(map(str, B)))
