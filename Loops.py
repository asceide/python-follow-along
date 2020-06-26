#Loops
nums = [1,2,3,4,5]

#For loops
#Looping through the nums list

for num in nums:
    print(num)

#Loop keywords
# Break - Breaks from the loop 
# Continue - Continues to the next iteration of the loop

for num in nums:
    if num == 3:
        print('found')
        break #breaks from the loop
    elif num == 4:
        continue #icontinues on to the next loop iteration
    print('num')

#Loop in a loop

for num in nums:
    for letter in 'abc':
        print(num, letter)

#To loop a number of times, use range()
for i in range(10):
    print(i)
#You can also start at an arbitrary number, but it now won't loop through the last number
for i in range(1,11):
    print(i) #prints the numbers 1 to 10

#While loops - like your normal while loops, with conditionals!
x = 0 
while x < 10:
    print(x)
    x +=1