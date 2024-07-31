import csv
path = r"S:\document pdf\color_code.csv"

with open(path,'r') as colorfile:
    data = csv.reader(colorfile, delimiter=",")
   #  print(type(data))
    for row in data:
        print(row)
      #   print(type(row))
        
    