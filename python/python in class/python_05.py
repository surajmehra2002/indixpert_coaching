set_1 = {"red", "black", "green"}
set_2 = {"yellow", "white", "red"}

data1 = set_1.union(set_2)
data2 = set_1.intersection(set_2)
data3 = set_1.difference(set_2)
data4 = set_2.difference(set_1)

result1 = "black" in set_1
result2 = "Black" in set_1

print(data1)
print(data2)
print(data3)
print(data4)
print(result1)
print(result2)