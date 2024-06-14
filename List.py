# A list is a data structure that is mutable(changeable), ordered sequence of elements
# create lists with [] - elements in the list are separated by commas
# every element has a position, those postions are called indexes
# indexes in lists start at 0 - first position will always be index 0

# declaring an empty list
empty_list = []

# list with stuff
# indexes    0             1             2
potions = ["Healing", "Invisiblity", "Strength"]
print(potions)

# accessing elements in a list by their index
# my_list[0] - access the first position in a list
# my_list[<number to indicate a position>]

#accessing our healing potion at index 0
print(potions[0]) #"Healing"

# accessing the invisibility potion at index 1
print(potions[1]) # "Invisibility"

# accessing the strength potion at index 2 - which is also the last index in this list
print(potions[2]) # "Strength"

# accessing the last position in a list will always be [-1]
# my_list[-1] <- last item in the list
print(potions[-1]) #Strength

# Python lists are very flexible
# many types can exist as elements in a list
#             0      1        2                3
cool_list = [42, "unicorn", 3.14, ["apple", "banana", "cherry"]]
#                                     0         1         2
print(cool_list)
# accesses the list at the last position or index 3 and then indexes into the list to get banana
print(cool_list[-1][1])
print(cool_list[3][1])

# LIST METHODS - appending, removing, popping, etc..
# my_list.append(<thing we're appending>)
# append will add to the back of the list

#           0           1           2        
names = ["Skylar", "Jeremiah", "Stephen"]
print(names)
names.append("Anthony")
print(names)
names.append("Anthony")
print(names)
names.append("Sydney")
print(names)
    # 0           1         2          3           4         5
# ['Skylar', 'Jeremiah', 'Stephen', 'Anthony', 'Anthony', 'Sydney']
# appending a new list with different data types to our list of strings
numbers = [1, 2, 3, 4, 5]
names.append(numbers) # names.append([1, 2, 3, 4, 5])
print(names)

# REMOVING elements from a list
# my_list.remove(<thing we're removing>)
names.remove("Sydney")
print(names)
names.remove("Anthony")
print(names)

# removing from a list within our list
# names[-1].remove(3)
# print(names)
# names.remove(numbers)
# print(names)

# POPPING an element from the list
# my_list.pop() <-- without an argument pop will remove the last element from the list
# my_list.pop(index) <-- a position to remove
# pop also returns the element that we're removing
popped_item = names.pop() #no argument so we pop the last index by default
print(popped_item)
print(names)
popped_item.append(6)
print(popped_item)

# popping with an argument
print(names.pop(1))
print(names)

# deleting by index
# del my_list[<index to delete>]
del names[1]
print(names)

# del with a variable
name = "Ryan"
print(name)
# del name[0]
# del name
# print(name)

# counting the number of occurences of an element in a list
# .count() 
# my_list.count(<the thing we're getting a count of>)
flowers = ["lily", "rose", "tulip", "lily", "daisy", "lily", "rose"]
print(flowers.count("lily"))
# setting a variable to a count
rose_number = flowers.count("rose")
print(rose_number)

# inserting items into our list
# my_list.insert(position, element)
hobbies = ["Kayaking", "Reading", "Working Out"]
print(hobbies)
hobbies.insert(1, "Video Games")
print(hobbies)
hobbies.insert(2, "Movies")
print(hobbies)
hobbies.insert(3, "Sketching")
print(hobbies)
# hobbies.insert("Running") TypeError - insert needs 2 arguments
hobbies.insert(9, "Basketball") #so if the position is greater than the length, it will placed at the end of the list
print(hobbies)
hobbies.append("Pokemon Cards")
print(hobbies)
# index error
# print(hobbies[7]) IndexError - list index out of range
# when we try to grab a position that doesnt exist in the list

# Preventing duplicate elements from being added to the list
# hobby = input("Enter a hobby to add to your list")
# # membership check in a list, checks to see if the element exists in the list
# # if <thing we're looking for> in list
# if hobby in hobbies:
#     print("that hobby already exists, we dont want any duplicates")
# else:
#     hobbies.append(hobby)

# print(hobbies)

# changing values at a specific index
#             0              1           2          3           4             5             6              7              8
hobbies = ['Kayaking', 'Video Games', 'Movies', 'Sketching', 'Reading', 'Working Out', 'Basketball', 'Pokemon Cards', 'Anime']
# accessing an element by index
print(hobbies[5])
hobbies[5] = "Hiking"
print(hobbies[5])
print(hobbies)

# Finding the index of an element in a list
# my_list.index(<element>)
position = hobbies.index("Movies")
print(position)
