# in below person is a class in which we can store multiple person with multiple methos
class person:
    name = "Suraj"
    occupation = "programmer"
    networth = 10

    # methods
    def info(self): # in this self is keyword, self means that object for which the method is being called
        print(f"{self.name} is a {self.occupation}")


# print(person.name)

a = person() # Create an instance/object of the person class

# a.name = "Deepak singh"

# print(a.name)

person.info()

