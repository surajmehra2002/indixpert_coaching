# one = [1,3,5,2,4]
# two = [10,2,4,5]

# output = [1,2,3,4,5,10]
# it mean combine=> remove duplicate=> sorting

one = [1,3,5,2,4]
two = [10,2,4,5]

output_with_duplicate = one + two

output_without_duplicate = []
for item in output_with_duplicate:
    if item not in output_without_duplicate:
        output_without_duplicate.append(item)

output_without_duplicate.sort()
print(output_without_duplicate)

