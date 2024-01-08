# python list

mylist = ['apple','mango','banana','mango'] # duplicate list
print(len(mylist)) # print the length of the list
print(mylist) # print the contents of the list
print(type(mylist))

# creating  a list using list constructor

mylist = list(('apple','mango','banana'))
print(mylist)

# accessing list items
mylist = ['john','james','mike']

# print the second item in the list
print(mylist[1])

# printing the last item in the list
cars = ['toyota','mercedes','range rover']
print(cars[2])
print(cars[-1]) # negative indexing

# range of indexes
DaysOfTheWeek = ['monday','tuesday','wednesday','thursday','friday','saturday']
print(DaysOfTheWeek[1:4]) # return item from position 1 (included) to 4 (not included)
print(DaysOfTheWeek[:5]) # range starts from first item by leaving out the start value
print(DaysOfTheWeek[2:]) # range goes to the end of the list by leaving out the end value

# range of negative indexes
animals = ['lion','leopard','cheetah','kangaroo','hyena']
print(animals[-4:-1]) # returns item in the list from -4 (included) to -1 (excluded/ not included)

# check if an item exists in a list
months = ['january','february','march','april']
if 'january' in months:
    print('yes, "january" exists')

# change item value in a list
numbers = [1,2,3,4,5,6,7]
numbers [1] = 10 # assigning new value at index 1
print(numbers)

# change range of item values
items = ['shoes','clothes','plates','spoons','knives']
items [1:3] = ['pans','cookers']
print(items)

# inserting more items than you replace
# the new items will be inserted where specified
# and the rest will move accordingly
items = ['shoes','curtains','trousers']
items [1:2] = ['printers','laptops']
print(items)

# inserting less items than you replace
# the new items will be inserted where specified
# and the rest will move accordingly
items = ['shoes','shorts','dress']
items[1:3] = ['boots']
print(items)

# inserting items into a list
phone =['samsung','apple','nokia']
phone.insert(2,'tecno')
print(phone)

# append items in a list
countries = ['south africa','kenya']
countries.append('uganda')
print(countries)

# extend list
fruits = ['mangoes','oranges']
tropical = ['pineapple','apple']
fruits.extend(tropical)
print(fruits)

# add any iterable
thislist = ['apple','mango']
thistuple = ['banana','sugar cane']
thislist.extend(thistuple)
print(thislist)

# remove list items
list = ['mango','apple','banana']
list.remove('banana') # remove specified item
print(list)
list.pop(1) # remove specified index
print(list)

list = ['mango','apple','banana']
list.pop() # removes the last item in the list when index is not specified
print(list)

# del keyword
years = [2001,2002,2003]
del years[1] # removes the specified index
print(years)
del years # deletes the list completely

# clear a list
number = [1,2,3.4,5,6.7]
number.clear()
print(number)

# loop through a list
numbers = [1,2,3,4,5,6]
for x in numbers:
    print(x)

# loop through the index numbers
numbers = ['one','two','three','four']
for x in range(len(numbers)):
    print(numbers[x])

# while loop
numbers = ['one','two','three','four']
i = 0
while i < len(numbers):
    print(numbers[i])
    i +=1

# looping using list comprehension
numbers = ['one','two','three','four']
[print(x )for x in numbers]

# create a new list  with only letter "v" in the list
vehicle = ['range rover','vanguard','mercedes','mark x','audi']
newlist = []
for x in vehicle:
    if 'v' in x :
        newlist.append(x)
print(newlist)
# with list comprehension
newlist = [x for x in vehicle if 'm' in x]
print(newlist)

# syntax  newlist = [expression for item in iterable if condition ==True]
#condition
newlist = [x for x in vehicle if x!='range rover' ] # only accept items that are not range rover
print(newlist)
# with no if statement
newlist = [x for x in vehicle]
print(newlist)

# using range function to create iterable
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x <5] # return only numbers lower than 5
print(newlist)

""" expression is the current item in the iteration but also the outcome you can manipulateber
it ends up like a list item  in the new list"""
# set the values in the newlist to upper case
newlist = [x.upper() for x in vehicle]
print(newlist)
# set the values in the newlist to "vehicles"
newlist = [ 'vehicles ' for y in vehicle]
print(newlist)

# expression containing condition to manipulate the outcome
"""return jeep instead of range rover"""
newlist = [x if x != 'range rover' else 'jeep' for x in vehicle] # return the item if it is not range rover if its range rover return jeep
print(newlist)

# sorting lists

# sorting alphabetically
mylist = ['orange','pawpaw','mango','banana','kiwi']
mylist.sort()
print(mylist)
# sort the list numerically
mylist = [ 100,1,3,800,1000,78,56]
mylist.sort()
print(mylist)
# sort list descending
mylist.sort(reverse = True)
print(mylist)

# customize sort function
""" sort the list on how numbers are close to 100"""
def myfunc(n):
    return abs(n -100)
mylist = [300,50,80,90,120]
mylist.sort(key= myfunc)
print(mylist)
# case insensitive sorting
""" sort is case sensitive and sorts capital letters before
lowercase letters"""
mylist = ['Orange','banana','Kiwi']
mylist.sort()
print(mylist)
# case insensiive sort
mylist.sort(key= str.lower)
print(mylist)

# reverse a list
mylist = [ 1,4,2,3,5,6,7,]
mylist.reverse()
print(mylist)
mylist.sort(reverse= True)
print(mylist)

# copying list
mylist = [1,2,3,4,5,6,7]
newlist = mylist.copy() # use of copy method
print(newlist)

# join lists
list1 = [ 1,2,3,4,5,6]
list2 =['a','b','c','d']
list3 = list2 + list1
print(list3)

list1 = [ 1,2,3,4,5,6]
list2 =['a','b','c','d']
for s in list2:
    list1.append(s)
print(list1)

list1 = [ 1,2,3,4,5,6]
list2 =['a','b','c','d']
list1.extend(list2)
print(list1)
