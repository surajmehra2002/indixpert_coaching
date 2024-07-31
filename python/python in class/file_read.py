path = r"S:\document pdf\text_file.txt"


# # First way:  
# data = open(path)
# # print(data)
# print(open(path).read())      #for read whole words
# print(open(path).read(10))    #for read 10 words including spacing
# open(path).close()            #it is necesorry to close file if open


# Second Way: 
with open(path,'r') as object:
    # print(type(object))
    # print(object.readline())    #for read first line
    # print(object.readlines())     #it print list and totle element in list will totle line in text file
    print(object.read())            #for read whole words