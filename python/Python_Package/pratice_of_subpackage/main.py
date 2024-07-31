# # use sub_package:
import my_package.module1 as e1
import my_package.module2 as e2

print(e1.country_vots())
print(e2.country_hitech())


# use my_package:
import my_package.sub_package.submodule1 as e1
import my_package.sub_package.submodule2 as e2

print(e1.state_india())
print(e2.state_Australiya())
