# FIRST WAY:

# class Person:
#     def __init__(self):
#         self.salary = 20000 
    
#     @property
#     def salary(self):
#         return self._salary

#     @salary.setter
#     def salary(self, value):
#         self._salary = 20000

#     def information(self):
#         return self.salary

# ob = Person()
# ob.salary = 1000 
# print(ob.information())  


# SECOND WAY:


class Person:
    def __init__(self):
        self.__salary = 20000 #private value
        self.salary = 20000 #public value
   

    def information(self):
        return self.__salary

ob = Person()
ob.__salary = 1000 
print(ob.information())  


