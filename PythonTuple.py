# python tuple
# create a tuple
mytuple = ('banana','orange','mango')
print(mytuple)

# tuple with duplicate values
mytuple = ('banana','mango','banana')
print(mytuple)

# tuple length
mytuple = ('banana','orange','mango')
print(len(mytuple))

# tuple with one item
""" to create a tuple with one item you have
to add a comma after the item  otherwise 
python will not recognise it as a tuple"""
mytuple = ('banana',)
print(type(mytuple))
# NOT  a tuple
mytuple = ('banana')
print(type(mytuple))

# tuple can be of any data type
tuple1 = ('apple','mango','orange')
tuple2 = (1,2,3,4,5)
tuple3 = (True,False)
print(tuple1,tuple2,tuple3)

# tuple with different data types
mytuple = ('banana','orange','mango',1,True)
print(mytuple)

#tuple constructor
mytuple = tuple(('apple','orange'))
print(mytuple)

# access tuple items
mytuple = ('banana','orange','mango','banana')
print(mytuple[2])

# negative indexing
mytuple = ('banana','orange','mango')
print(mytuple[-1])

# range of indexeds
mytuple = ('banana','orange','mango')
print(mytuple[0:3])

#leaving out the start index
mytuple = ('banana','orange','mango')
print(mytuple[:3])

#leaving out the end index
mytuple = ('banana','orange','mango','pawpaw')
print(mytuple[2:])

# range of negative indexes
mytuple = ('banana','orange','mango')
print(mytuple[-2:-1])

# check if item exists
mytuple = ('banana','orange','mango')
if 'banana' in mytuple:
    print('yes it exists')

# change tuple values
""" tuples are unchangeable or immutable once
created. but you can work  around and change the tuple into 
a list , change the value  and change  the list back to a tuple"""

mytuple = ('banana','orange','mango')
mylist = list(mytuple)
mylist [1] = 'kiwi'
mytuple = tuple(mylist)
print(mytuple)

# add items to tuple

# one way is converting the tupls into a list and back to a tuple
mytuple = ('banana','orange','mango')
y = list(mytuple)
y.append('kiwi')
mytuple = tuple(y)
print(mytuple)

# another way is adding tuple to a tuple
mytuple = ('banana','orange','mango')
y = ('kiwi',)
mytuple += y
print(mytuple)

# remove items

# convert the tuple to a list and back to a tuple
mytuple = ('banana','orange','mango')
x = list(mytuple)
x.remove('orange')
mytuple =tuple(x)
print(mytuple)

# delete the tuplt completely
mytuple = ('banana','orange','mango')
del mytuple
print('deleted')

# unpack tuples

# assigning values to tuple is called packing
mytuple = ('orange','banana','pawpaw','avocado','apple')
print(mytuple)

# extracting values back into a variable from a tuple is called unpacking
mytuple = {'orange','mango','apple'}
(green, yellow,red) = mytuple
print(green,yellow,red)

# using an asterisk when the number of variables is less than number of values in the tuple
mytuple = ('orange','banana','pawpaw','avocado','apple')
(green,yellow,*red) = mytuple
print(green)
print(yellow)
print(red)

# using an asterisk in another variable other than the last
mytuple = ('orange','banana','pawpaw','avocado','apple')
(green,*yellow, red) = mytuple
print(green)
print(yellow)
print(red)

# LOOPING THROUGH TUPLE

#using for loop
mytuple = ('orange','banana','pawpaw','avocado','apple')
for x in mytuple:
    print(x)

# looping through index numbers
mytuple = ('orange','banana','pawpaw','avocado','apple')
for i in range(len(mytuple)):
    print(mytuple[i])

# using while loop
mytuple = ('orange','banana','pawpaw','avocado','apple')
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i += 1

mytuple = ('orange','banana','pawpaw','avocado','apple','orange')
print(mytuple.index('avocado'))
print(mytuple.count("orange"))