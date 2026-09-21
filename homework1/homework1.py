#File: homework1.py



# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, a number with a real and imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, an ordered collection of items

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, an unordered collection of key-value pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an ordered collection of items that cannot be changed

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, an ordered collection of items

i = True
print(i)
print(type(i)) # i is a boolean, a value that can be either True or False

j = None
print(j)
print(type(j)) # j is a NoneType, a special type that represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, an ordered collection of items

l = str(14)
print(l)
print(type(l)) # l is a string, a sequence of characters

m = 1e4
print(m)
print(type(m)) # m is a float, a number with decimals


'''
Questions:

1. How many different data types did you find?
    9 different data types

2. List all the data types you found.
    int
    float
    complex
    str
    list
    dict
    tuple
    bool
    NoneType

3. What variables have the same data types?
    a and l are both int
    b and m are both float
    e, h, and k are lists

4. What was the data type of l? Why is it not an integer? What does str() do?
    The data type of l is str
    It is not an integer because of str() 
    The str() function converts the integer 14 to a string "14"

5. Look up one more data type not given above. Repeat the same procedure.
'''
n = range(5)
print(n)
print(type(n)) # n is a range, a sequence of numbers generated over a specified range



# --- Booleans ---

print(10 > 9) # True, 10 is greater than 9

print(10 == 9) # False, 10 is not equal to 9

print(10 <= 9) # False, 10 is not less than or equal to 9

print(bool("abc")) # True, non-empty strings are considered True

print(bool(123)) # True, non-zero numbers are considered True

print(bool(["apple", "cherry", "banana"])) # True, non-empty lists are considered True

print(bool(True)) # True, the boolean value True is considered True

print(bool(False)) # False, the boolean value False is considered False

print(bool(0)) # False, the number 0 is considered False

print(bool("")) # False, empty strings are considered False

print(bool(" ")) # False, strings with only whitespace are considered False

print(bool(())) # False, empty tuples are considered False

print(bool([])) # False, empty lists are considered False

print(bool({})) # False, empty dictionaries are considered False

print(bool(True and False)) # False, True and False is considered False

print(bool(True and True)) # True, True and True is considered True

print(bool(False and False)) # False, False and False is considered False

print(bool(True or False)) # True, True or False is considered True

print(bool(True or True)) # True, True or True is considered True

print(bool(False or False)) # False, False or False is considered False

print(bool(not(False))) # True, not False is considered True

print(bool(not(True))) # False, not True is considered False


'''
Questions:

1. What pattern do you notice about expressions returning True or False?
    Besides simple logic answers, data types that are empty or zero return False, 
    while non-empty or non-zero data types return True.

2. Which expression surprised you about its result?
    I was surprised thtat bool(" ") returned False, because I thought that a string with 
    spaces in it would be considered True.

3. Create an expression, not given above, that will return True. Why is it True?
'''
string1 = "good"
string2 = "good"
string3 = "bad"

print(bool(string1 == string2)) # True, because string1 is equal to string2
'''
4. Create an expression, not given above, that will return False. Why is it False?
'''
print(bool(string1 == string3)) # False, because string1 is not equal to string3



# --- Operators ---

# - Arithmetic Operators -

print(10 + 5) # 15, + performs addition

print(10 - 5) # 5, - performs subtraction

print(2 * 4) # 8, * performs multiplication

print(6 / 3) # 2.0, / performs division

print(5 % 2) # 1, % performs modulus, which returns the remainder of a division

print(3 ** 2) # 9, ** performs exponentiation, which raises a number to the power of another number

print(15 // 2) # 7, // performs floor division, which returns the rounded down result of a division

# - Comparison Operators -

print(5 == 2) # False, == checks if two values are equal

print(10 != 10) # False, != checks if two values are not equal

print(2 < 5) # True, < checks if the left value is less than the right value

print (12 > 5) # True, > checks if the left value is greater than the right value

print(5 <= 6) # True, <= checks if the left value is less than or equal to the right value

print (1 >= 10) # False, >= checks if the left value is greater than or equal to the right value

# - Assignment Operators -

x = 5

x += 5 # x = x + 5, += adds the right value to the left value and assigns the result to the left value

x -= 4 # x = x - 4, -= subtracts the right value from the left value and assigns the result to the left value

x *= 3 # x = x * 3, *= multiplies the left value by the right value and assigns the result to the left value

# - Logical Operators -

'''
Questions:

1a. What does the operator "and" do? 
    The "and" operator returns True if both expressions are True, and False otherwise.
1b. Write an expression that results in True. Write an expression that results in False.
'''
bool1 = True
bool2 = True
bool3 = False

print(bool(bool1 and bool2)) # True, because both bool1 and bool2 are True

print(bool(bool1 and bool3)) # False, because bool3 is False
'''
2a. What does the operator "or" do?
    The "or" operator returns True if at least one of the expressions is True, and False otherwise.
2b. Write an expression that results in True. Write an expression that results in False.
'''
print(bool(bool1 or bool3)) # True, because bool1 is True
print(bool(bool2 or bool3)) # True, because bool2 is True
print(bool(bool3 or bool3)) # False, because both bool3 values are False
'''
3a. What does the operator "not" do?
    The "not" operator returns the opposite boolean value of the expression it is applied to.
3b. Write an expression that results in True. Write an expression that results in False.
'''
print(bool(not bool3)) # True, because bool3 is False and not False is True
print(bool(not bool1)) # False, because bool1 is True and not True is False

'''
More Questions:
1. What is the difference between / and //?
    The / operator performs division and returns a float
    The // operator performs floor division and returns an integer that is rounded down to the nearest whole number.
2. What is the difference between % and //?
    The % operator performs modulus and returns the remainder of a division
    The // operator performs floor division and returns an integer that is rounded down to the nearest whole number.
3. What operator would you use to calculate the remainder when dividing two numbers? Give an example.
    The % operator would be used to calculate the remainder when dividing two numbers.
    Example: 10 % 3 = 1, because 10 divided by 3 is 3 with a remainder of 1.
4. How do assignment operators work?
    Assignment operators take the value on the right and performs an operation to the variable on the left 
    It then assigns that value to the variable
'''



# --- Strings ---

my_string = "hello"

print(my_string) # Prints: hello

print(my_string[0]) # Prints: h

print(my_string[1]) # Prints: e

print(my_string[2]) # Prints: l

print(my_string[3]) # Prints: l

print(my_string[4]) # Prints: o

print(my_string[-1]) # Prints: o

print(my_string[1:3]) # Prints: el

print(len(my_string)) # Prints: 5

print(my_string + "goodbye") # Prints: hellogoodbye

print(my_string * 7) # Prints: hellohellohellohellohellohellohello

'''
Questions:
1. Define the term slicing. For which of the manipulations did you slice your string?
    Slicing is the process of extracting a portion of a string by specifying a range of indices
    print(my_string[1:3]) printed "el"

2. Call the following, describe the result:
'''
name = "Oski"
print("Hello, my name is", name) # Prints: Hello, my name is Oski
'''
3. Call the following, describe the result:
'''
name = "Oski"
print(f"Hello, my name is {name}") # Prints: Hello, my name is Oski
'''
4. What is the difference between the two last print statements?
    The first print statement adds the variable after the string
    The second print statement uses an f-string, which allows you to add the variable into the string
'''



# --- Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# Lists the contents of the current directory
# Example: ls

# ls -a
# Lists all contents of the current directory, including hidden files
# Example: ls -a

# mkdir
# Creates a new directory
# Example: mkdir new_folder

# cat
# Displays the contents of a file
# Example: cat file.txt

# pwd
# Prints the current working directory
# Example: pwd

# cd ..
# Moves up one directory level
# Example: cd ..

# cd .
# Moves down one directory level
# Example: cd .

# cd ~
# Moves to the home directory
# Example: cd ~

# cp
# Copies a file or directory
# Example: cp file.txt new_file.txt

# mv
# Moves a file or directory
# Example: mv file.txt new_file.txt

# rm
# Removes a file or directory
# Example: rm file.txt

# clear
# Clears the terminal screen
# Example: clear

# grep
# Searches for a specific pattern in a file or output
# Example: grep "pattern" file.txt

'''
1. Look up 3 other commands not present. Define and explain how to use them on the command line
    python: runs a Python script
        Example: python script.py
    nano: opens a text editor in the terminal
        Example: nano file.txt
    rmdir: removes an empty directory
        Example: rmdir empty_folder
2. What is the difference between ls and ls -a?
    ls lists the contents of the current directory
    ls -a lists all contents of the current directory, including hidden files
3. What is a hidden file?
    A hidden file is a file that is not normally visible in the file system. 
4. Look up 3 other flags (e.g., -a was a flag for the ls command). 
   Define and explain how to use them on the command line
    -l: lists the contents of the current directory in long format, including file permissions, ownership, size, and modification date
        Example: ls -l
    -h: displays file sizes in human-readable format (e.g., KB, MB, GB)
        Example: ls -lh
    -r: reverses the order of the output
        Example: ls -r
'''
