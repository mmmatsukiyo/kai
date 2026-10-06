# File: homework4.py



# 3 --- Lists ---


# 3.1 - List Operations -

favorite_foods = ["pizza", "sushi", "ice cream", "tacos", "pasta"]

# 1
print(favorite_foods[1])

# 2
print(favorite_foods[-1])

# 3
favorite_foods.append("burgers")

# 4
favorite_foods.insert(0, "apple")

#5
favorite_foods.remove("ice cream")

# 6
print(len(favorite_foods))

# 7
for food in favorite_foods:
    print(food.upper())

# 8
top_favorites = favorite_foods[::len(favorite_foods) - 1]

#9
for food in favorite_foods:
    if "potato" in food:
        print("A potato!")
    else:
        print("No potato!")


# 3.2 - Slicing and Striding - 

numbers = list(range(0,21))

# 1
def get_first_15(numbers):
    return numbers[:15]

# 2 
def get_every_5th(lst):
    lst = get_first_15(lst)
    return lst[::5]

# 3
def reverse_and_stride(lst):
    lst = get_every_5th(lst)
    lst = lst[::-1]
    return lst[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)


# 3.3 - Nested Lists -

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

numbers = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]

# 3.3.1 - Nested List Operations -

# 1
print(numbers[2])

# 2
print(numbers[1][1])

# 3
numbers.append([10, 11, 12])

# 4
def sum_nested(lst):
    total = 0
    for i in lst:
        for j in i:
            total += j
    return total


# 3.4 - Create a 5x5 List -

def create_5x5_list():
    lst = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(i * 5 + j + 1)
        lst.append(row)
    return lst

# 1
def remove_multiples_of_3(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] % 3 == 0:
                lst[i][j] = "?"
    return lst

lst1 = remove_multiples_of_3(create_5x5_list())

# 2
def sum_of_non_multiples_of_3(lst):
    total = 0
    for sublist in lst:
        for num in sublist:
            if num != "?":
                total += num


    return total

sum1 = sum_of_non_multiples_of_3(lst1)



# 4 --- Dictionaries ---



# 4.1 - Dictionary Operations -

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

# 1
print(ages["Katie"])

# 2
ages["Mira"] = 100

# 3
ages["Milana"] = 52

# 4
ages.pop("Mariam")

# 5
for name, age in ages.items():
    print(name, age)




'''
Genuinely, I didn't have any errors when doing this I'm so locked in
However, I did check my code multiple times to ensure it was printing/returning everything that I wanted
Instead, I'll talk about where I had some trouble in ensuring I was following the instructions correctly.

1. It took me a second to realize lists use .append() to add seomthing to it, rather than something else like .add() which is used for Java

2. I had to look back at the videoes to figure out how dictionaries worked since we didn't have much time to work on them

3. It took me a second to figure out that .pop() was how you removed something from a dictionary
'''


# Favorite function!!
print(create_5x5_list())