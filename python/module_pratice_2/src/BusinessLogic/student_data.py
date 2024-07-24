import sys,os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../HUB/')))
# sys.path.append(os.path.join(os.path.dirname(__file__), '..','HUB'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../HUB'))


# print(sys.path)
# print(type(sys.path)) #this is type list
# sys.path.append(os.path.join(os.path.dirname(__file__), '../HUB'))
# print(type(os.path.join(os.path.dirname(__file__), '../HUB')))

import hitech
import vots

print(hitech.students())
print(vots.students())