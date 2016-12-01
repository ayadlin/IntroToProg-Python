import DataProcessor, Persons, Contacts, Employees, Customers

print("Test the DataProcessor.File class")
objDP = DataProcessor.File()
objDP.FileName = "Test.txt"
objDP.TextData = "This is a test"
strMessage = objDP.SaveData()
print(strMessage)

print("\n Test the DataProcessor.Database class")
try:
    print("Trying to create an object, but the class is not ready")
    objDP = DataProcessor.Database()
except:
    print("This should fail")


print("\n Test the Persons.Person class")
objP = Persons.Person()
objP.FirstName = "Bob"
objP.LastName = "Smith"
print(objP.ToString())

print("\n Test the Contacts.Contact class")
objCt = Contacts.Contact()
objCt.FirstName = "Bob"
objCt.LastName = "Smith"
objCt.St = "Prospect"
objCt.Nu = 80
objCt.App = "A"
objCt.ZipC = "02143"    # Zip code has to be input as string
                        # becuase python does not allow integers
                        # that start with 0
objCt.Ph = 16178523431
objCt.Em = "bob@smith.com"
print(objCt.ToString())


print("\n Test the Customers.Customer class")
objC = Customers.Customer()
objC.Id = 1
objC.FirstName = "Bob"
objC.LastName = "Smith"
objC.St = "Prospect"
objC.Nu = 80
objC.App = "A"
objC.ZipC = "02143"
objC.Ph = 16178523431
objC.Em = "bob@smith.com"
objC.CC = 1234567890123456
objC.ED = 1020
objC.CVC = 113
print(objC.ToString())

print("\n Test the Employees.Employee class")
objE = Employees.Employee()
objE.Id = 1
objE.FirstName = "Bob"
objE.LastName = "Smith"
print(objE.ToString())

print("\n Test the Customer.CustomerList class")
objCL = Customers.CustomerList()
try:
    print("Trying the wrong object type")
    objCL.AddCustomer(objP)
except:
    print("This should fail")

try:
    print("Trying the wrong object type")
    objCL.AddCustomer(objCt)
except:
    print("This should fail")
    
try:
    objCL.AddCustomer(objC)
    print("Trying the correct object type")
    print(objCL.ToString())
except:
    print("This should work")



print("\n Test the Employee.EmployeeList class")
objEL = Employees.EmployeeList()
try:
    print("Trying the wrong object type")
    objEL.AddEmployee(objP)
except:
    print("This should fail")
    
try:
    objEL.AddEmployee(objE)
    print("Trying the correct object type")
    print(objEL.ToString())
except:
    print("This should work")

