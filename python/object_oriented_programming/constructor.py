# CONSTRUCTOR
# A constructor in a class is used to initialize an object’s properties when the object is created. It allows you to set up the initial state of the object.


# Without constructor code
# class person:
#     name = "Suraj singh"
#     occ = "HR"

#     def info(self):
#         print(f"{self.name} is {self.occ}")

# obj = person()

# obj.name = "manoj"
# obj.occ = "developer"
# obj.info()

# obj.name = "shyam"
# obj.occ = "programmer"
# obj.info()


# with constructor code
class person:
    def __init__(self, n, o): #self means that obj/ instance for which being called
        print("hello this is constructor")
        self.name = n
        self.occ = o

    def information(self):
        print(f"{self.name} is a {self.occ}")
    
obj1 = person("suraj", "programmer")
obj2 = person("manoj", "developer")

obj1.information()
obj2.information()
