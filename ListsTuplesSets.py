#Lists
#To create a list, you use squared brackets, and within them you add values, unless you want an empty list in which case you leave it as is
courses = [] #Empty List
courses = ['History', 'Math', 'Physics', 'CompSci']
#To get the length of a list, you still use len()
#You can use negative indexes to start at the end of a list, which starts with the index of -1
print(courses[-1])


#Slicing
#You can also get a range of values within an index by including x:y inside of the square brackets. The range starts at x and ends at y-1
print(courses[0:2])
#You can also exclude 0 if you plan to start from the start of the list
print(courses[:2])
#You can start from an index to the last element of a list by exluding the second number
print(courses[2:])

#List functions
#To add an item to the end of a list, use append
courses.append('Art')
#To insert an item at a specific index in a list, use insert which takes in two arguments: The index and value. This doesn't ovver
courses.insert(0,'Art')

#If you are going to add the values from a second list to the first list, use extend()
courses2=['Art', 'Biology']
courses.extend(courses2)

#Removing from lists
#You can use remove specific items from a list by using remove
courses.remove('Math')
#alternatively you can use pop, which removes the last value by default and returns the index of that valye
courses.pop()

#Sorting the lists
#If you want to reverse a list, you can use the reverse function
courses.reverse()
#You can use the sort method to sort the list as well
courses.sort() #It sorts by ascending order. If you want to do it descending order, you can pass an argument within the sort method, sort(reverse=True)
#If you want to sort without changing the original list, use sorted() which returns a sorted list
sorted_courses=sorted(courses)

#Min, Max, Sum
min(arg) #Returns the smallest number in a list
max(arg) #Returns the largest number in a list
sum(arg) #Returns the sum of all the numbers in a list

#Searching
#You can search for the index of a value using index(arg), for example
courses.index('CompSci')
#If you want to check if a value is in a list, use in
'Math' in courses #True
'Art' in coureses #False

#This for loop means that the value of item is equal to the value of the enumerated index in courses until it reaches the end of a list
for item in courses:
    print(item)
#If you want to get the index of the value while iterating through a list, use enumerate
for index, course in enumerate(courses):
    print(index, course)
#If you want to start in another index, you can use a second argument in enumerate
for index, course in enumerate(courses, start=1):
    print(index, course)

#If you want to turn a list into a string with a value, use the join method
course_str = ', '.join(courses) #Type the string that you want each value of a string to be separated by, and use the join method with that.
#If you want to split a string into a list, use the split method which takes in an argument of the string that will be used to separate the string
new_list = course_str.split(' - ')

#Tuples
#Tuples are like lists, but they are immutable meaning they cannot be changed
#Tuples are declared with paranthesis instead of squared brackets
tuple_1=('History,', 'Math', 'Physics', 'CompSci')
#The only methods that can be use with Tuples are those that aren't used for mutations

#Sets are unordered, unique lists. They do not contain duplicate values. They are declared with curly brackets
courses={'History', 'Math', 'Physics', 'Compsci', 'Math'}

#Sets automatically remove duplicates
#Like in tuples, you can use in to check whether a value is in the set
'Math' in courses #returns true

#You can also see whether a value in one set is also located within another set
courses2={'History', 'Math', 'Art', 'Design'}

courses.intersection(courses2) #Returns values that are common between two sets
courses.difference(courses2) #Returns values from the first set that isn't in the second set
courses.union(courses2) #Returns all the values from both sets

#Empty lists
elists=[] 
elists=list()

#Tuples
etuples=()
etuples=tuple()

#Sets
eset=set() #You cannot use {} since that declares an empty dictionary