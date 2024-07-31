# import my_package  #in this case my_package will directry not module

# print(my_package.vots())  #we have to minded that there will be some module(file)between directry(my_package) and method(function) vots() because function can't within folder. you can see file name in which vots methods using ctrl+click in method(vots)
# print(my_package.hitech())

# second way:
import my_package.module1 as e
print(e.vots())
