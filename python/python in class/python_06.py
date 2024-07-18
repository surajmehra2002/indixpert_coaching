tupple_01 = (10, 20, 30, 40, 50)

try:
    tupple_01[2]=30
except TypeError as e:
    print(e)

print(tupple_01)