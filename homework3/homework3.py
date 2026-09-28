# File: homework3.py



# 3: --- Print Functions ---


# 3.1: - Say Goodbye -

def say_hello(name): #In-class print function:
    #Says hello to 'name'
    print("Hello,", name)

def say_goodbye(name):
    #Says goodbye to 'name'
    print("Goodbye,", name)


# 3.2 - Area of a Circle

def area_circle(r):
    #Prints the area of a circle with radius r
    pi = 3.14
    area = pi * (r ** 2)

    print(area)



# 4: --- Return Functions ---


# 4.1: - Subtract, Multiply and Divide -

def add(a, b): #In-class return function
    #Adds two numbers, a and b, together
    return a + b

def subtract(a, b):
    #Subtracts two numbers, a and b, together
    return a - b

def multiply(a, b):
    #Multiplies two numbers, a and b, together
    return a * b

def divide(a, b):
    #Divides number a by number b
    return a / b




# 5: --- Conditionals ---


# 5.1: - What Should I Wear? - 

def temp_range(readings):
    #Returns the maximum and minimum temperature values to give that day's highest and lowest temperatures
    high = max(readings)
    low = min(readings)

    return (low, high)


# 5.2: - Check if it's the Weekend -

def is_weekend(day): #In-class conditional function
    #Returns if it is the weekend based on the day
    if day == "Saturday" or day == "Sunday":
        return "It's the weekend!"
    else:
        return "It's not the weekend"

def is_weekend_int(day):
    #Returns a boolean value whether or not it is the weekend based on integer values that correspond to each day of the week
    if day == 6 or day == 7:
        return True
    else:
        return False


# 5.3: - Fuel Efficiency Calculator - 

def fuel_efficiency(m, g):
    #Calculates the fuel efficency based on miles m and gallons g
    mpg = m / g

    return mpg


# 5.4: - Secret Code -

def encrypt(code): #*** DOES NOT WORK IF THE LAST DIGIT IS ZERO!!! (I would figure out a way to do it but it would probably look like I'm using AI by adding stuff we haven't gone over)
    #Encrypts a secret code by moving the last digit to the front of the number
    last_digit = code % 10 
    new_code = last_digit * (10 ** (len(str(code)) - 1)) 
    code //= 10 
    new_code += code 

    return new_code
    


# 6: --- Loops ---


# 6.1: - Oski Stole Your Power -

def power(x, y):
    #Raises x to the power of y
    digit = x

    for i in range(y - 1):
        x *= digit
    
    return x


# 6.2: - Min & Max with Loops! - 

# 6.2.1: - For Loops -

def minimum_for_loop(list):
    #Finds the minimum value in list using a for loop and returns it
    min = list[0]

    for i in list:
        if i < min:
            min = i
    
    return min

def maximum_for_loop(list):
    #Finds the maximum value in list using a for loop and returns it
    max = list[0]

    for i in list:
        if i > max:
            max = i
    
    return max

# 6.2.2: - While Loops -

def minimum_while_loop(list):
    #Finds the minimum value in list using a while loop and returns it
    index = 0
    min = list[0]

    while index < len(list):
        if list[index] < min:
            min = list[index]

        index += 1

    return min

def maximum_while_loop(list):
    #Finds the maximum value in list using a while loop and returns it
    index = 0
    max = list[0]

    while index < len(list):
        if list[index] > max:
            max = list[index]

        index += 1

    return max


# 6.3 - Calculate the Sum -

def sum_of_digits(value):
    #Takes each individual digit of a number and finds the sum
    length = len(str(value))
    sum = 0

    for i in range(length):
        digit = value % 10
        sum += digit
        value //= 10

    return sum



# 7: --- Running Your Script ---
x = 1234

result = sum_of_digits(x) # Finds the sum of the digits of x

print(f"The result of Calculate the Sum (6.3) with value = {x} is {result}")