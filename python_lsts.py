'''
Lists are ordered collection of data items.
They store multiple items in a single variable.
List items are separated by commas and enclosed within square brackets [].
Lists are changeable meaning we can alter them after creation.

'''

lst = [[1, 4, 3, ("New Chapter Beginning", "Back to Normal Life")], [{'like': 'cake', 'dislike': 'beinggettingfooled','love':'Varun'}], ["I Love Water Activities", "I Love Travelling", "I Love Exploring Nature", "I Love Honesty", "I Love Chocolates", "Last but not the least I Love Varun Kacholia"]]

print(lst[2][-1])

print(lst[2][-1])

lst1 = lst[2][-1].split()

print(lst1[7])


if 'Varun' in lst1[7]:
    print("Yes, He is active !!!")
else:
    print("He is missing !!!")

letter_a = [a for a in lst1 if "a" in a]

print(letter_a)

l_a = [[j for j in i if "a" in str(j)] for i in lst]

print(l_a)

print(lst1)

lst1.sort(reverse = True) # Small Letters with higher range will come first and then capital letters.

print("Sorted List: ", lst1)

print(lst1.index("Varun"))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

colors.insert(0, 'pink')
print(colors)

#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow) # This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
print(colors)

colors = ["voilet", "indigo", "blue", "green"] # Concatenating 2 lists.
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)


