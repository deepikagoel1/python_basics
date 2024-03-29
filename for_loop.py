
# iterating over a string:

name = 'Varun Kacholia'

for i in name:
    # print(i, end=", ")
    print(i, end = '')
    

food = ['chinese', 'indian', 'continental']
print()

for i in food:
    print(i, end ='\t')

print()

for i in range(len(food)):
    print(food[i], end = " ")