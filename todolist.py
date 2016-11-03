# Assignment 5
# By Alejandro Wolf-Yadlin, October 31, 2016


# This program manages a to do list
# The list contains two columns of data ("Task" and "Priority"
# The lsts will be managed suing a python dictionary



todolist = {}                               # Define empty dictionary "todolist"
                                            # Open ToDo.txt to read as a variable name "todo"
with open("ToDo.txt") as todo:              # will close todo when loop is done
    for line in todo:
       line =line.strip()                   # will remove '\n' at end of new line
       (task, priority) = line.split(',')   # Separate task and priority by comma
       Task=task                            # Define task in dictionary
       todolist[Task] = priority            # Assign pritority to task in dicitionary


todotable = []                              # Define empty dictionary "todolist"                           

for key, value in todolist.items():         # Trsansfer keys and values from dictionary to list
    todotable.append([key,value])


# This section prints the starting state of the to do list
# as it was read from ToDo.txt, with headers 'Task' and 'Priority'
print('Your current Tasks and Prioriteis are:')
print('Task         ', 'Priority')
for line in todotable:
    print(line[0],'    ',line[1])

# This section provides the user 3 options:
# add task to the to do list
# remove tasks from the to do list
# Save the todo list to ToDo.txt

choice = 0                                  # Define dummy variable choice
conditions = ('1', '2', '3')                # Define valid answers for user to input
                               

# The while loop below will keep running unless the user chooses to save his/her to do list

while choice != 3:                          # choice  = 3 means save list as is now                         
    print ("\nChoose 1 to Add task")
    print ("Choose 2 to Remove task")
    print ("Choose 3 to Save all tasks to the Todo.txt file and exit!")
    choice = input('What would you like to do?: ')    

# if the user inputs an invalid choice, ask them to input valid one
    if choice not in conditions: 
        print('\nPlease select choice 1, 2 or 3: ')
    else:

# convert choice from str to integer so it can be compared to numerical values
        choice = int(choice)               


# if the user chooses to add a task append it at end of list and dictionary
        if choice == 1:
            nt = str(input("\nWhat is your new task?: "))
            np = str(input("What is its priority?: "))
            todotable.append([nt,np])           # list
            todolist[nt]=np                     #dictionary
            print('\nyour new task:', nt,'has been added to your to do list with priority', np) 
# if the user choses to remove a task            
        elif choice == 2:
            tr = str(input("\nWhat task do you want to remove?: "))
            removed = 0                        # Define dummy variable removed
            for t in todotable:                 # iterate through the table lines           
                if tr in t[0]:                  # if the task is in any line
                    todotable.remove(t)         # remove that line
                    print(tr,' has been removed\n')
                    removed = 1
            if removed != 1:
                print('\nYour choice is not available, lets start again: ')


todotable.sort(key=lambda x:x[0])               # Sort the list by task alphabetically
todolist =dict(todotable)                       # Save the list as dictionary 



# Print to screen the 
print('\nYour modified Tasks and Prioriteis are:\n')
print('Task         ', 'Priority')
myfile = open("ToDo.txt", "w")         # create/open text file, with writing privileges
for line in todotable:                          
    print(line[0],'    ',line[1])
    task = ','.join(str(x) for x in line)
    myfile.write(task + '\n')
myfile.close()

input('Your to do list has been saved, please press any key to exit')
