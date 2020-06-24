#Dictionaries
#Dictionaries are declared within a curly bracket with the key-value pair seprated by a colon
student={'name':'John', 'age':25, 'courses':['Math','CompSci']}
#In order to access the various elememnts of a dictionary, pass in the key as an argument in squared brackets after the variable name
student['name']
student['age']
student['courses']
#Or rather, to avoid errors you can use get() method in order to get a value. If the key doesn't exist then the method returns 'None'
student.get('name')#Returns John
student.get('Phone') #Returns none
#To set a default return value with get, pass in a second argument with the default value
student.get('Phone', 'Not Found')

#Adding to a dictionary
#Add to dictionary by declaring the value in square brackets and attributing a value to it
student['phone'] = '555-5555' #Also overwrites whatever value a key had if it already exists

#You can also use update method to accomplish so. It takes in a dictionary of things you want to update
student.update({'name': 'Jane', 'age':26, 'phone':'555-5555'})

#Deleting
#Like adding, you use the variable name with the key that is to be deleted held within a square bracket. However the variable name must be preceded by del
del student['age']
#pop method can also be used to remove a key and return a value

age = student.pop('age') #Returns the value in age when it is popped

#You can use len() to see the length of a dictionary
print(len(student))

#To find the keys of a dictionary using keys()
student.keys()

#To get dictionary values, use values()
student.values()

#For the entire dictionary key-values, use items()
student.items()

#In order to iterate through the dictionary....

for key in student: #Just prints the keys in the dictionary
    print()
for key, value in student.items(): #In order to print both the keys and values you use the items() method 

#So basically in a for loop, how ever number of values are returned by the statement after the in is how many number of variables you can use before the in. What variable is which depends on what the statement returns.