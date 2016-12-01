#-------------------------------------------------#
# Title: CustomerApp
# Dev:   ayadlin
# Date:  11/30/2016
# Desc: This application manages customer data
# ChangeLog: modified from Rroot EmployeeApp
#
#-------------------------------------------------#
if __name__ == "__main__":
    import DataProcessor, Customers, os
else:
    raise Exception("This file was not created to be imported")

#-- Data --# 
# declare variables and constants
objC = None                 # a Customer object
intId = 0                   # a Customer Id
gIntLastId = 0              # Records the last CustomerId used in the client
strFirstName = ""           # a Customer's first name
strLastName = ""            # a Customer's last name
strStreet = ""              # a Customer's street name
strNumber = 0               # a Customer's street #
strAppartment = ""          # a Customers Appartmnet
strZip = 00000              # a Customer's Zip Code
strPhone = 0000000000       # a Customer's Phone number
strEmail = ""               # a Customer's e-mail
strCC = 0000000000000000    #a Customer's credit card number
strED = 0000                # a Customer's credit card expiration date
strCVC = 000                # a Customer's credit card security code
strUserInput = ""           # temporary user input
strInput = ""               # temporary user input
DataFile = "CustomerData.txt"

#-- Processing --#
#perform tasks
def ProcessNewCustomerData(Id, FirstName, LastName, St, Nu, App, ZipC, Ph, Em, CC, ED, CVC):
    try:
        #Create Customer object
        objC = Customers.Customer()
        objC.Id = Id
        objC.FirstName = FirstName
        objC.LastName = LastName
        objC.St = St
        objC.Nu = Nu
        objC.App = App
        objC.ZipC = ZipC
        objC.Ph = Ph
        objC.Em = Em
        objC.CC = CC
        objC.ED = ED
        objC.CVC = CVC
        Customers.CustomerList.AddCustomer(objC)
    except Exception as e:
        print(e)

def GetDataFromFile():
        """Reads data"""
        try:
            objRF = DataProcessor.File()
            objRF.FileName = DataFile
            if os.path.exists('./' + objRF.FileName):
                a =objRF.GetData()
                return a
            else:
                print("the file does not exist, you'll have to create it \n")
        except Exception as e:
            print("Python reported the following error: " + str(e))
        #return a

a = GetDataFromFile()


# Find current ID in actual data file
try:
    a
    ID = a.rsplit(',',10)[1]
    ID = int(ID.rsplit('\n',1)[1])
    #print(ID) # test
    if isinstance(ID,int):
        gIntLastId = ID
    else:
        gIntLastId = 0
except:
    gIntLastId = 0


def SaveDataToFile():
    try:
        objF = DataProcessor.File()
        objF.FileName = DataFile
        if os.path.exists('./' + objF.FileName):
            objF.TextData = Customers.CustomerList.ToString()
            print("Reached here")
            objF.SaveData()
        else:
            objF.TextData = "Id, FirstName, LastName, Number, Street, App, Zip, Phone, E-mail"\
                         " Credit Card #, Exp. Date, Security Code \n" + \
                         Customers.CustomerList.ToString()
            print("Reached it")
            objF.SaveData()
    except Exception as e:
        print(e)

#-- Presentation (I/O) --#
#__main__
        
#get user input
while(True): 
  strUserInput = input("Would you like to add Customer data? (y/n) ")
  if(strUserInput == "y"):
      # Get Customer Id from the User
      intId = int(input("Enter a Customer Id (Last id was " + str(gIntLastId) + "): "))
      gIntLastId = intId    
      # Get Customer FirstName from the User
      strFirstName = str(input("Enter a Customer First Name: "))
      # Get Customer LastName from the User
      strLastName = str(input("Enter a Customer Last Name: ") )                        
      # Get Customer Street Name from the User
      strStreet = str(input("Enter a Customer Street Name: ") ) 
      # Get Customer Street Number from the User
      strNumber = int(input("Enter a Customer Street Number: "))  
      # Get Customer Appartment from the User
      strAppartment = str(input("Enter a Customer Appartment: ") ) 
      # Get Customer zipcode from the User
      strZip = str(input("Enter a Customer Zip Code: ") ) 
      # Get Customer Phone Number from the User
      strPhone = int(input("Enter a Customer Phone Number: "))
      # Get Customer Email from the User
      strEmail = str(input("Enter a Customer e-mail address: "))
      # Get Customer Credit Card Number from the User  
      strCC = int(input("Enter a Customer Credit Card Number: "))
      # Get Customer Credit Card Expiration Date from the User
      strED = int(input("Enter a Customer Credit Card expiration date (mmyy): "))
      # Get Customer Credit Card Security Code from the User
      strCVC = int(input("Enter a Customer Credit Card Security Code (3 or 4 digits): "))
  
      #Process input
      ProcessNewCustomerData(intId, strFirstName, strLastName, strStreet, strNumber, strAppartment,\
                             strZip, strPhone, strEmail, strCC, strED, strCVC)
  else:
      break 

#send program output
print("\nThe Data your adding is: ")
print("------------------------")
print("Id, FirstName, LastName, Number, Street, App, Zip, Phone, E-mail"\
      " Credit Card #, Exp. Date, Security Code \n" + \
      Customers.CustomerList.ToString())

#get user input
strInput = input("Would you like to save this data to the data file?(y/n) ")
if(strInput == "y"):
    SaveDataToFile()
    #send program output   
    print("data saved in file")
else:
    print("Data was not saved")

a = GetDataFromFile()
print("\nThe current database saved is: \n")
print(a)
print("This application has ended. Thank you!")

