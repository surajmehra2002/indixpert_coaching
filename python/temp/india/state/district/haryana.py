# FIRST WAY:

import sys
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '../../../indixpert/hitech/batch/batch1/'))
sys.path.append('s:\\indixpert_coaching\\python\\temp/indixpert/hitech/batch/batch1/')
# sys.path.append(os.path.join(os.getcwd(), r"indixpert/hitech/batch/batch1/"))
# sys.path.append('Path of module file')

import student 
print(student.hitech())



# # SECOND WAY:

# import sys 
# import os 
# # sys.path.append(os.path.join(os.getcwd(),r"indixpert//hitech\batch/batch1\\")) # r means you can use /,//,\,\\ python will tri to understand path type
# # sys.path.append(os.path.join(os.getcwd(),"indixpert/hitech/batch/batch1/"))
# sys.path.append(os.path.join(os.getcwd(),"indixpert\\hitech\\batch\\batch1\\"))

# # print("\n os.getcwd: ",os.getcwd()) #It means that folder location which opened in vs code
# # print("\nsys.path: ",sys.path)      #It means that folder location in which this file are located, it type list so you can append more path as a list

# import student

# # print("Hitech Data")
# print(student.hitech())
