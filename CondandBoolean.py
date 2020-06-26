#Boolean and Conditionals
if True: #Simple If statement
    print("Hello")

language = "Python"
if language == "Python": #There is no need for a function to evaluate strings in Python
    print('Conditional was True')

#Object Identity uses is. is checks if objects are the same objects in memory
#If else statements
if language == "Python" :
    print("True")
elif language == "Java":
    print("True") 
else:
    print("False")
#Python doesn't have switch statements

#Boolean operations and, or, not (equivalent to &&, || and !)

user = 'Admin'
logged_in = True

if user=='Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad credentials')

a = [1,2,3]
b = [1,2,3]

print(a==b) #Evaluate true since the the values inside each array are the same
print(a is b) #Evaluates to False since the two objects have different locations within memory
print(id(a)) #id() can be used to get the memory address of an object
#False Values include:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence, such as '', (), []
    # Any empty mapping, like {}