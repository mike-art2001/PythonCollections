# python sets
# created using curly braces
myset = {'apple','orange','banana'}
print(myset)

# sets do not allow duplicates
myset = {'apple','orange','banana','orange'}
print(myset)

# values True and 1 are considered same and treated as duplicates in sets
myset = {'apple','orange','banana',2,True,1}
print(myset)

# values False and 0 are considered same and treated as duplicates in sets
myset = {'apple','orange','banana',2,False,0}
print(myset)

# get the length of a set
myset = {'apple','orange','banana',2,True}
print(len(myset))

# set items - data types
myset = {'apple','orange','banana'} # set of  string data type
myset1 = {1,2,3,4,5,6} # set of  int data type
myset2 = {True , False,False} # set of boolean data type
print(myset)
print(myset1)
print(myset2)

# type() method
myset = {'apple','orange','banana',2,True}
print(type(myset))

# set() constructor
myset = set(('apple','orange','banana'))
print(myset)

# access set items
#using for loop
myset = {'apple','orange','banana',2,True,1}
for x in myset:
    print(x)

# check if item exists in  a set
myset = {'apple','orange','banana',2,True,1}
print('banana' in myset)

# add items to sets

# using the add() method to add one item to a set
myset = {'apple','mango'}
myset.add('orange')
print(myset)

# add sets
myset = {'apple','mango'}
newset = {1,2,3}
myset.update(newset)
print(myset)

# add any iterable
""" the update method doesnt take only set objects
but it take any iterable i.e lists, tuples, dictionaries"""
myset = {'apple','orange'}
mylist = [1,2,3,4,5]
myset.update(mylist)
print(myset)

# remove items

# using remove() method
""" if the item being removed does not exist remove raises an error"""
myset = {'apple','orange','mango'}
myset.remove('apple')
print(myset)
# using discard() method
""" if the item being removed does not exist discard method will not raise an error"""
myset = {'apple','orange','mango'}
myset.discard('apple')
print(myset)
# using pop() method
""" pop removes random item"""
myset = {'apple','orange','mango'}
myset.pop()
print(myset)

# clearing a set
myset = {'apple','orange','mango'}
myset.clear()
print(myset)
# deleting a set
myset = {'apple','orange','mango'}
del myset
print('deleted')

# loop sets
# loop using for loop
myset = {'apple','orange','mango'}
for x in myset:
    print(x)

# joining two sets
# using union() method
myset = {'apple','orange','mango'}
myset1 = {1,2,3,4}
myset2 = myset.union(myset1)
print(myset2)
# using update() method
myset = {'apple','orange','mango'}
myset1 = {1,2,3,4}
myset.update(myset1)
print(myset)

# keep only the duplicates
myset = {'apple','orange','mango'}
myset1 = {"apple",'banana','mango'}
myset.intersection_update(myset1)
print(myset)
# using intersection()
myset = {'apple','orange','mango'}
myset1 = {'apple','banana','mango'}
myset2 = myset.intersection(myset1)
print(myset2)

#keep all but not the duplicates
myset = {'apple','orange','mango'}
myset1 = {'apple','banana','mango'}
myset.symmetric_difference_update(myset1)
print(myset)
# using symmetric_difference()
myset = {'apple','orange','mango'}
myset1 = {'apple','banana','mango'}
myset2 = myset.symmetric_difference(myset1)
print(myset2)