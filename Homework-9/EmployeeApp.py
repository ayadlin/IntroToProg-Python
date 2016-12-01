#-------------------------------------------------#
# Title: EmployeeApp
# Dev:   RRoot
# Date:  12/12/2020
# Desc: This application manages employee data
# ChangeLog: (Who, When, What)
#
#-------------------------------------------------#
if __name__ == "__main__":
    import DataProcessor, Employees
else:
    raise Exception("This file was not created to be imported")

#-- Data --# 
# declare variables and constants
objE = None #an Employee object
intId = 0 #an EmployeeId
gIntLastId = 0 #Records the last EmployeeId used in the client
strFirstName = "" #an Employee's first name
strLastName = "" #an Employee's last name
strInput = "" #temporary user input

#-- Processing --#
#perform tasks
def ProcessNewEmployeeData(Id, FirstName, LastName):
    try:
        #Create Employee object
        objE = Employees.Employee()
        objE.Id = Id
        objE.FirstName = FirstName
        objE.LastName = LastName
        Employees.EmployeeList.AddEmployee(objE)
    except Exception as e:
        print(e)

def SaveDataToFile():
    try:
        objF = DataProcessor.File()
        objF.FileName = "EmployeeData.txt"
        objF.TextData = Employees.EmployeeList.ToString()
        print("Reached here")
        objF.SaveData()
    except Exception as e:
        print(e)
 
#-- Presentation (I/O) --#
#__main__
        
#get user input
strUserInput = ""
while(True): 
  strUserInput = input("Would you like to add Employee data? (y/n)")
  if(strUserInput == "y"):
      #Get Employee Id from the User
      intId = int(input("Enter an Employee Id (Last id was " + str(gIntLastId) + "): "))
      gIntLastId = intId
      #Get Employee FirstName from the User
      strFirstName = str(input("Enter an Employee First Name: "))
      #Get Employee LastName from the User
      strLastName = str(input("Enter an Employee Last Name: ") )                        
      #Process input
      ProcessNewEmployeeData(intId, strFirstName, strLastName)
  else:
      break 

#send program output
print("The Current Data is: ")
print("------------------------")
print(Employees.EmployeeList.ToString())

#get user input
strInput = input("Would you like to save this data to the dat file?(y/n)")
if(strInput == "y"):
    SaveDataToFile()
    #send program output   
    print("data saved in file")
else:
    print("data was not saved")

print("This application has ended. Thank you!")

