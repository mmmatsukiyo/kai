# File: homework5.py



# 2 --- Homework 1 + 2 Review ---


# 2.1 - Vocabulary Review -
'''
1. Git vs GitHub
    Git allows you to track changes in your code
    GitHub is a website that uses Git where you can share code and collaborate with others

2. Terminal vs. Command Line
    The terminal is a text-based interface that lets you interact with the operating system
    The command line is within the terminal where you type and execute commands

3. Local vs. Remote Repository
    A local repository is a version of your code that is stored on your computer
    A remote repository is a version of your code that is stored on a server

4. Version Control
    Version control records changes to a files so that you can recall specific versions later

5. Staging Area
    The staging area is where you can prepare changes to be committed to the repository

6. git add
    git add adds changes in your working directory to the staging area (put stuff in a box)

7. git commit
    git commit saves changes from the staging area to the local repository (wrap the box and label it)

8. git push
    git push uploads the changes from the local repository to a remote repository (send the box on its way)

9. git status
    git status displays the state of the working directory and the staging area

10. git pull
    git pull fetches and downloads content from a remote repository and immediately updates the local repository

11. pwd
    pwd (print working directory) displays the current directory you are in

12. ls
    ls lists the contents of a directory

13. cd
    cd (change directory) helps you move between directories

14. nano
    nano opens the nano text editor, which allows you to create and edit text files from the terminal

15. touch
    touch creates an empty file

16. mv
    mv moves or renames files and directories

17. rm
    rm removes files or directories

18. cat
    cat concatenates and displays the contents of files.
'''
    

# 2.2 - A Directory Tree -

'''
1. You have been plopped into Judy's directory system. What command will tell you what your current working directory is?
    pwd

2. The terminal responds by saying you are in ~/python_decal/judy decal. What command will list all the files in your current working directory?
    ls

3. Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py. You will need to pull the brianna repo repository to find the updated file. What command(s) will let you move to the correct repository and pull the latest changes?
    cd ../brianna_repo
    cd brianna_repo
    git pull

4. How would you move this new homework.py to the homework/ folder in your personal repository?
    mv homework.py ~/python_decal/judy_decal/homework/

5. How would you move yourself to the same repository as homework.py?
    cd ..
    cd judy_decal/homework

6. You want to see the contents of homework.py in your terminal, how would you do this?
    cat homework.py

7. Great job! You just finished the homework for this week. What command(s) allow you to save the changes and push from your local repository to your remote repository?
    git add .
    git commit -m "Finished homework"
    git push

8. Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did “Judy” do wrong when trying to push?)
    git pull
    git push

9. What absolute path will allow you to move to Recents/?
    cd ~
    cd Recents
'''

# 2.2 - Draw Your Directory Tree -

'''
In homework5 folder
'''


# 3 --- Homework 3 Review --- 


# 3.1 - Data types -

def checkDataType(var):
    if type(var) == int:
        return "int"
    elif type(var) == float:
        return "float"
    elif type(var) == complex:
        return "complex"
    elif type(var) == str:  
        return "str"   
    elif type(var) == list:
        return "list"
    elif type(var) == dict:
        return "dict"
    elif type(var) == tuple:
        return "tuple"
    elif type(var) == bool:
        return "bool"
    elif type(var) == type(None):
        return "NoneType"

# 3.2 - Condictions -

def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"



# 4 --- Loops ---

def sumWithLoop(list):
    total = 0
    for i in list:
        total += i
    return total



# 5 --- Homework 4 Review ---


# 5.1 - Lists -

def duplicateList(list):
    newList = []
    for i in list:
        newList.append(i)
        newList.append(i)
    return newList


# 5.2 - Debugging -

'''
def square(num)   <- There is no semicolon
    return num * num
'''

def square(num):
    return num * num




# Favorite function:

var = None

def checkDataType(var):
    if type(var) == int:
        return "int"
    elif type(var) == float:
        return "float"
    elif type(var) == complex:
        return "complex"
    elif type(var) == str:  
        return "str"   
    elif type(var) == list:
        return "list"
    elif type(var) == dict:
        return "dict"
    elif type(var) == tuple:
        return "tuple"
    elif type(var) == bool:
        return "bool"
    elif type(var) == type(None):
        return "NoneType"


print(f"The variable var is a {checkDataType(var)}")