# Data types
integer = 1

floating = 3.14

boolean = True

string = "hello world!" 

num_string = "4" # this is also a string

array = [1,2,3,4,5] # note: arrays can contain any of the other data types - not just integers
# strings are also kind of like arrays

# elements in arrays can be accessed like so:
array_elem = array[0] # keep in mind that arrays start at 0, not 1

# So we can also have:
type_array = [1, 3.14, True, "hello",[1,2,3,4,5]]

dictionary = {"key":"value"} # dictionaries can also contain any other type of variable
print(dictionary['key'])

#######################################################################################
# Operators - pretty self explanatory... except for one

result = 1 + 2
#print(result)

result = 10 - 5
#print(result)

result = 10 / 2
#print(result)

result = 10 * 10
#print(result)

result = 10 % 2 # <--- the % is called a modulo. it essentially returns the remainder. 
# In this example if we divide 10 by 2 there should be no remainder

result =  11 % 2 # here there is a remainder
#print(result)

# Why is this useful?


result = "python" + "pilled" # operators also work with other data types... python tries its best to make it work
#print(result)

result = "hi " * 10
#print(result)

result = 1 + 3.14 # here we are adding an int and a float 
#print(result)

result = [1,2,3] + [4,5,6]
#print(result)


##################################################
# Comparisons. These return booleans since they are either true or false
# > 
# < 
# >= 
# <=
# == Equals. Note that python (and other languages) use a DOUBLE equals sign. 
# != Does not equal

# [condition] and [condition] returns true if both conditions are true
# [condition] or [condition] returns true if one condition is true
# 
# [condition] and not[condition] - not can be used to invert the truth value of something

#print(10 > 1)

res = True and True

res = (3 > 1) and ((10 + 1) == 11)
#print(res)


########################################################################################
# Important commands

print("hello") # pretty self explanatory - prints stuff to the console. We're gonna use this alot. Accepts pretty much any variable type


l = len(array) # Returns the number of items in an array, dictionary or string. Returns an int
#print(l) # should say 5

#preference = input("What is your name? ") # Input asks the user to input a command. Always returns a string.

variable = type(floating) # returns the type of variable. Useful for debugging
#print(variable)


r = range(0, 10) # generates a range of numbers from 0 to 10. Important for loops. Returns an object (dont worry about this for now)



# stuff you should try. I know the answers to some of these are obvious but its a good exerice


# does "mochi" have 6 letters? Print a boolean

# print the first and last letters of "mochi" using indexing... do not cheat by doing print("mi") 


# is 44 * 25.8 bigger than 1000? Print a boolean


# Ask the user to input a number, return True if its even and False if its not. Print a boolean


# add the numbers in the array together. Print an integer
nums = [69, 420]

# Make a basic calculator. Ask the user to input 2 numbers, then print out their sum, difference, product, and quotient

