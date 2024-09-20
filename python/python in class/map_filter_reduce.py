
# #MAP
# # if i want currection each in every item then this will help
# def cube(x):
#     return x*x*x

# print(cube(2))

# l = [1,2,3,4,5,6]

# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# # print(newl)

# # newl = list(map(cube, l))  #map(function name, list)
# newl = list(map(lambda x: x*x*x, l))  #lambda yesa method jo x lena and cube return krega

# print(newl)




#FILTER

def func(a):
    return a>10

l = [1,2,3,4,5,6,3,60,28,10]
# if i want a list in which every item grater than 10 then filter method use

newl = list(filter(func, l))
print(newl)





