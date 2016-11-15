#--------------------------------------------------------------#
# Title: Working with Functions, Pickle, Shelve and Exceptions
# Dev:   ayadlin
# Date:  November 14, 2016
# ChangeLog: (Who, When, What)
#   Based on RRoot, 11/02/2016 Assignment 5 solution
#   Based on ayadlin 11/07/2016 Assignment 6 solution
#   Homework 7 specific code will be framed as ##################
#                                                   code        #
#                                                   code        #   
#                                                   code        #
#                                              ##################
#---------------------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority, Number} # Number is added as function of priority
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#

# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

# Importing modules pickle and shelve

import pickle, shelve, os

# Global Variables

FileName = "C:\_PythonClass\ToDo.txt" # Default File to read and write to.
BinFile= "C:\_PythonClass\ToDo" # Python adds the .dat when working with binary
BinFilePath = "C:\_PythonClass\ToDo.dat"
strData = ""
dicRow = {}
lstTable = []



# Prologue
# Function 0
# This function assigns a numerical value to the different levels of priority
# 1 for high, 2 for medium and 3 for low - All other options will be assigned 4
# We will use this function to sort our to do list by order of priority

def numerizepriority(x=dicRow):
            if x["Priority"] == "high":
                x["Number"] = 1
            elif x["Priority"] == "medium":
                x["Number"] = 2
            elif x["Priority"] == "low":
                x["Number"]=3
            else:
                x["Number"]=4


# First I will group all functions within a class I'll call list managmenet

class listmanagement():
    """ This class contains methods for processing simple 2 column lists """
    
    
# Function 1
# Make a fucntion to load the task/priority list into a dictionary and then a list

    def loadtodolist(objFileName = FileName):
        """
        This function loads a to do list from a txt file
        :Input: file.txt
        :Default input: C:\_PythonClass\ToDo.txt
        """
        objFile = open(objFileName, "r")
        for line in objFile:
            strData = line.split(",") # readline() reads a line of the data into 2 elements
            dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
            numerizepriority(dicRow)
            lstTable.append(dicRow)
        objFile.close()

# Here we wuse a lambda function to sort the to do list according to priority
        lstTable.sort(key=lambda x:x["Number"])

# The function will return our list
        return(lstTable)    

# HOMEWORK 7 PICKLING AND SHELVING OPENING FROM A BINARY FILE - ALSO EXCEPTIONS
#################################################################################
                                                                                #
# Function 1a - for homework 7 using shelving                                   #                
# Make a fucntion that loads tasks/priority list from a .dat file               #
    def loadBINtodolist(objFileName = BinFile):                                 #
                                                                                #
# Check that file name and path are correct and open using shelve               #
        try:                                                                    #        
            f = shelve.open(BinFile,'c')                                        #
        except():                                                               #
# If file name.path are not correct send a message and exit the program         #
            print("""Your program will close now, please check that your          
file and name and path are correct and try again""")                            #                                                                         
            exit()                                                              #     
                                                                                #
# if the file exists and it is not empty read it and build lstTable             #
        if os.path.exists(BinFilePath) and os.path.getsize(BinFilePath) > 0:    #                                                                    
            Tasks = f["Task"]                                                   #
            Priorities = f["Priority"]                                          #     
            for l in range(0, len(Tasks)):                                      #
                dicRow = {"Task":Tasks[l],"Priority":Priorities[l]}             #
                numerizepriority(dicRow)                                        #    
                lstTable.append(dicRow)                                         #
                                                                                #    
# Here we wuse a lambda function to sort the to do list according to priority   #
            lstTable.sort(key=lambda x:x["Number"])                             #
                                                                                #
        else:                                                                   #
            print("The file is currently empty")                                #
        #print(Tasks)                                                           #
        #print(Priorities)                                                      #
        #print(lstTable)                                                        #
        f.close()                                                               #
                                                                                #
# The function will return our list                                             # 
        return(lstTable)                                                        # 
                                                                                #
#################################################################################





# Function 2
# Make a fucntion to display current tasks

    def currenttasks(task = lstTable):
        """
        This function prints the todo list liaded from the text file above
        :Input: No input
        """
        print("\n******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
            #return(lstTable)


# Function 3
# Make a fucntion that adds a new item to the list/Table

    def addtask():
        """
        This function adds tasks to our to do list
        :Input: no input
        """
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|medium|low] - ")).strip()
        dicRow = {"Task":strTask,"Priority":strPriority}
        numerizepriority(dicRow)
        lstTable.append(dicRow)
            
# Here we wuse a lambda function to sort the updated to do list according to priority
        lstTable.sort(key=lambda x:x["Number"])
        return(lstTable)

# Function 4
# Make a function that remove an item from the list/Table
    @staticmethod           # Not sure if this is needed?
    def removetask():
        """
        This function rmoves tasks to our to do list
        :Input: no input
        :Default input: C:\_PythonClass\ToDo.txt
        """
            #4a-Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False #Creating a boolean Flag
        intRowNumber = 0
        while(intRowNumber < len(lstTable)):
            # Modified if to make task at least 3 characters long (it was erasing
            # first task when input left blank or space bar was used)
            if(len(strKeyToRemove) > 2 and strKeyToRemove in str(lstTable[intRowNumber])): 
                del lstTable[intRowNumber]
                blnItemRemoved = True
                #end if
            intRowNumber += 1
            #end while loop
            #4b-Update user on the status
            #print(lstTable)    
            if(blnItemRemoved == True):
                print("The task was removed.")
            else:
                print("I'm sorry, but I could not find that task.")
            return(lstTable)
            

# Function 5
# Make a fucntion that save the tasks to the ToDo.txt file

    def savetodolist(objFileName = FileName):
        """
        This function adds tasks to our to do list
        :Input: file.txt where to do list will be saved
        
        """
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")


# HOMEWORK 7 PICKLING AND SHELVING STORING in Binary file
#################################################################################
                                                                                #        
# Function 5a - for homework 7 using shelving                                   #                
# Make a fucntion that save the tasks/priority list to                          #
# the ToDo.dat file as a set of lists                                           #
    def saveBINtodolist(objFileName = BinFile):                                 #
                                                                                #
# open dat file using shelve                                                    #
        s = shelve.open(BinFile,'n')                                            #
        Tasks=[]                                                                #
        Priorities = []                                                         #
        NumPriorities = []                                                      #
        print(lstTable)                                                         #
                                                                                #
# Create list containing Tasks and priorities, Numpriorities optional           #
        for row in lstTable:                                                    #
            Tasks.append(row["Task"])                                           #
            Priorities.append(row["Priority"])                                  #
            #NumPriorities.append(row["Number"])                                #
                                                                                #
# Assign the list to s and thus to the the datfile called when s was opened     #                                                                           #        
        s["Task"] = Tasks                                                       #        
        s["Priority"] = Priorities                                              #
        s["Number"] = NumPriorities                                             #            
                                                                                #
# sync the contents of s to the dat file                                        # 
        s.sync()                                                                #
        print(s["Task"])                                                        #
        print(s["Priority"])                                                    #
        print(s["Number"])                                                      #
        s.close()                                                               #
                                                                                #    
#################################################################################






###############################################################################################################################
# Now that functions are written develope the same code as for assignment 5,
# but using the 5 functions defined above            
   

# Define a single funcion that run the other functions from listmanagement class together
def runall(objFileName = FileName):


# AT THE BEGGINING OF THE PROGRAM WE ALLOW THE USER TO CHOSE IF (S)HE'LL READ THE DATA FROM A .TXT OR .DAT FILE
#################################################################################################################
                                                                                                                #
# Use function 1 from listmanagement class to Load table from file                                              # 
    while(True):                                                                                                #                    
        filetype = str(input("Press 1 if you are reading from a from a.txt file, 2 if from a .dat file "))      #
        if filetype =='1':                                                                                      #
            lstTable = listmanagement.loadtodolist()                                                            #
            break                                                                                               #
        elif filetype =='2':                                                                                    #
            lstTable = listmanagement.loadBINtodolist()                                                         #
            break                                                                                               #
        else:                                                                                                   #
            print("Please enter 1 for .txt or 2 for .dat files")                                                #
            continue                                                                                            #
                                                                                                                #
#################################################################################################################
        
# step 2 Provide menu of options and run functions

    while(True):
        print ("""
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)

# HOMEWORK 7 EXCEPTION HANDLING
#############################################################################################
                                                                                            #
# This is homework 7 part a -use try and except                                             #
## I modified homework 6 so the options are entered as integers and handle failure          #
# of the user to input an integer with a ValueError Exception                               #
                                                                                            #
# First three lines - try to get any integer from the user                                  #
# if the user provide an inetger print an empty line before proceding in the loop           #
                                                                                            #
        try:                                                                                #
            intChoice = int(input("Which option would you like to perform? [1 to 5] - "))   #
            print()#adding a new line                                                       #
# If the user does not provide an integer handle the exception with a ValueError            #
# Print new line urging the user to use an integer value between 1 and 5                    #
# And use continue to go back to the beggining of the while loop and start the menu again   #
                                                                                            #    
        except(TypeError, ValueError):                                                      #
            print('\nPlease enter an integer between 1 and 5')                              #
            continue                                                                        #
                                                                                            # 
#############################################################################################



    # Step 3 use function 2 from listmanagement class to show the current items in the table
        if (intChoice == 1):
            listmanagement.currenttasks()
            continue #to show the menu

    # Step 4 use function 3 from listmanagement class to add a new item to the list/Table
        elif(intChoice == 2):
            listmanagement.addtask()
            listmanagement.currenttasks()
            continue #to show the menu

    # Step 5 use function 4 from listmanagement class to remove an item from the list/Table
        elif(intChoice == 3):
            #removetask()
            listmanagement.currenttasks()
            listmanagement.removetask()
            listmanagement.currenttasks()
            continue #to show the menu

# AT THE BEGGINING OF THE PROGRAM WE ALLOW THE USER TO CHOSE IF (S)HE'LL READ THE DATA FROM A .TXT OR .DAT FILE
#################################################################################################################
                                                                                                                #
    # Step 6 use function 5 from listmanagement class to save tasks to the ToDo.txt file                        #
        elif(intChoice == 4):                                                                                   #
            listmanagement.currenttasks()                                                                       #
            while(True):                                                                                        #
                filetype = str(input("Press 1 if you are saving to a.txt file, 2 if to a .dat file "))          #
                if filetype =='1':                                                                              #
                    lstTable = listmanagement.savetodolist()                                                    #
                    break                                                                                       # 
                elif filetype =='2':                                                                            #
                    lstTable = listmanagement.saveBINtodolist()                                                 #
                break                                                                                           # 
            else:                                                                                               #
                print("Please enter 1 for .txt or 2 for .dat files")                                            #
                continue                                                                                        # 
                                                                                                                #  
            continue #to show the menu                                                                          #
                                                                                                                #
#################################################################################################################

    # Step 7 get out of program if user wants to exit
        elif (intChoice == 5):
            break #and Exit the program

        else:
            print('please provide a valid option: an integer between 1 and 5\n')
            continue


# Call runall to view/modify the to do list
runall()



