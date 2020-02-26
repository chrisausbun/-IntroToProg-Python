# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog, Completed the To-Do sections and now have a fully functioning script:
# RRoot,1.1.2030,Created started script
# Chris Ausbun,02-19-20,Added code to complete assignment 5
# Chris Ausbun,02-26-20,Added part of the code to get remove working by adding Task ID integers
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"  # An object that represents a file
objFile = open(strFile, "r")  # file handle
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
intTaskID = 0
flgUpdateIDs = False
flgTaskFound = False

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.

for row in objFile:
    lstRow = row.split(",")
    dicRow = {"ID": lstRow[0], "Task": lstRow[1], "Priority": lstRow[2].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #

# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        objFile = open(strFile, "r")
        for item in lstTable:
            print(item.get("ID"), item.get("Task"), item.get("Priority"), sep=",")
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        while True:
            for item in lstTable:
                print("Please type a task or type 'Exit' to quit! ")
                strTask = input("Task (Example: Watch TV): ")
                if strTask == item.get("Task"):
                    flgTaskFound = True
                    print("Task already exists, please enter a new one")
                break
            if not flgTaskFound:
                strPriority = input("Priority (Example: Low): ")
                intTaskID = len(lstTable)
                intTaskID += 1
                dicRow = {"ID": intTaskID, "Task": strTask, "Priority": strPriority}
                lstTable.append(dicRow)
                flgTaskFound = False
                print("Data Added!")
                strUserSaveChoice = input("Would you like to continue adding tasks? (y/n):  ")
                if strUserSaveChoice.lower() == "n":
                    flgTaskFound = False
                break
            flgTaskFound = False

    # Step 5 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        while True:
            ExistingTask = input("Please type the number of row you'd like to remove: ")
            for objRow in lstTable:
                if ExistingTask in objRow.values():
                    print("Removing this task from the list: " + ExistingTask)
                    lstTable.remove(objRow)
                    flgUpdateIDs = True
            if flgUpdateIDs is True:
                intTaskID = 0
                for objRow in lstTable:
                    intTaskID += 1
                    objRow.update({"ID": str(intTaskID)})
                flgUpdateIDs = False
            elif flgUpdateIDs is False:
                print("Task Row Not Found!")
            strUserSaveChoice = input("Would you like to continue removing tasks? (y/n): ")
            if strUserSaveChoice.lower() == "n":
                flgUpdateIDs = False
                break

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        print("Would you like to save and exit, or exit without saving?")
        strChoice = str(input("Please type 'Y' for Yes, or 'N' for No: "))
        if strChoice.upper() == "Y":
            objFile = open(strFile, "w")
            for item in lstTable:
                objFile.write(
                    str(item.get("ID")) + "," + str(item.get("Task")) + "," + str(item.get("Priority")) + "\n")
            print("Data Saved!")
            objFile.close()
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting Now!")
        break  # and Exit the program
