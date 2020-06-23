message = 'Hello World' #Variable holding a String
message = "Hello World" #Can also use double quotes for strings. Difference between the two depends on the usage of the string. For example
#message = 'Hello's World' would create an error. This can be circumvented by either using double quotes on a string that uses single quotes, or escape using \ like in 'Hello\'s World'
message = """Hello's World was a
 good cartoon in the 1990s""" #This creats a multiline string by enclosing it within three double quotes

##If you want to access different characters within a string (remember its an array), follow the variable name with []
#For Example
message[0] #Would get the the character at the first index of the string
#In order to get a range of characters within a string, use the following slices
message[x,y] #X is the beginning index, Y is the end index of the slice. However, X is excluded while Y is included.
message[0,5] #Gets the string from that slice range
message [5:] #Gets the slice from the starting index to the end of the string
message[:5] #Gets the slice from the start of the string to the end index

#Different String Functions
len() #Length function to figure out the length of a string
message.count('') #This function counts how many times a character or string subset occurs in a string
message.find('') #Returns the index of a character in a string, or the starting index of a substring in string
#Notice that these functions return a new string.
message.lower() #Lowercase the string
message.upper() #Uppercase the string
message.replace('','') #Replaces a substring with another substring and returns a new string

#Joining strings 
greeting = 'Hello'
name = 'Patrick'
message = greeting + name #Joins the strings
message = greeting + ', ' + name #Suppose you need to format a string
message = '{}, {}. Welcome!'.format(greeting, name) #You can use placeholders to format strings and concatenations

#fstrings - for Python 3.6 and above, allows variables to be used directly with a string
message - f'{greeting}, {name.upper()}. Wecome!' #You can use functions directly with variables if using fstring'

#you can use dir(x) if you want to know what functions you can use with a variable.