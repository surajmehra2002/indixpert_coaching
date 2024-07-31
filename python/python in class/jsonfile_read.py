import json

path = "S:/dwsample2-json.json"

# data = json.load(open(path, "r"))
data = json.loads(open(path,"r").read())

# in json.load(here will come json file type like io file which is open(path))
# in json.loads(str format of dict) both work samly


print(data.keys())
d= json.dumps(data) #it convert dict data into str.
d1= json.loads(d)
print(d1.keys())




