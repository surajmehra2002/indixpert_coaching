import json

path = r"S:\indixpert_coaching\python\data_storing_files\dwsample2-json.json"

# data = json.load(open(path, "r"))
data = json.loads(open(path,"r").read())

# in json.load(here will come json file type like io file which is open(path))
# in json.loads(str format of dict) both work samly

# print(path)
# print(type(path))
# print(data)
# print(type(data))
# print(json.dumps(data))
print(type(json.dumps(data)))
print(type(json.loads(json.dumps(data))))

# print(data.keys())
# d= json.dumps(data) #it convert dict data into str where data is dict and d is str.
# d1= json.loads(d)#it convert str dict data into dict(d=str,d1=json/dict).
# print(d1.keys())




