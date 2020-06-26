#Functions
#Functinons start with def, otherwise its pretty much like any other function
def hello_func():
    pass #This keyword allows you to make a blank function without the compilier throwing an error
    return 'Hello Function.' #Obviously returns a function 

#You;re able to chain functions like in 
hello_func().upper() ##Outputs the return statement in uppercase

#Passing Parameters
def hello_func(greeting):
    return '{} Function'.format(greeting)

print(hello_func('Hello')) #Returns Hello Function.

#Adding default values if the function doesn't take in a parameter

def hello_func(greeting, name = 'You'): #The default value is declared in the argument parameter list
    return '{}, {}'.format(greeting, name)

#Positional arguments - Use * and ** when you don't know how many arguments and keywords will be passed through the parameters. * are for args, ** are for keywords.
#Keywords are arguments that are set with a preceding name. I.E. name = 'Patrick', while a normal argument is just a variable or number or what have you
def student_info(*args, **kwargs): #args and kwargs are conventional names
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name: 'John', 'age':32}

#if you want to pass each member of a dictionary, list etc, individually to a function with positional parameters, use * and ** when calling the functions

student_info(*courses, **info)

# Number of days per month, First value placeholder for indexing purposes.
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """Returns True for leap years, False for non-leap years."""

    return year%4 == 0 and (year % 100!=0 or year%400 == 0)

def days_in_month(year, month):
    """Returns number of days in that month"""

    if not 1<=month<=12:
        return 'Invalid Month'

    if month==2 and is_leap(year):
        return 29

    return month_days[month] 