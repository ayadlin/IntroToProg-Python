#Data
objFile = None #File Handle
strUserInput = None #A string which holds user input

# The first class creates a new inventory obeject/reads it
class Inventory(object):
    def __init__(self, name, Id=0, product=0, Price=0):
        self.name = name # the name of the inventory needs to be provided when calling an inventory object 
 
    def WriteProductUserInput(self,File):
      try:
        print("Type in a Product Id, Name, and Price you want to add to the file")
        print("(Enter 'Exit' for Id to quit!)\n")
        while(True):  
          Id= input("Enter Id: ")
          if(Id.lower() == "exit"): break
          else:
              self.Id = Id
              self.product = input("Enter Name: ")
              product =str(self.product)
              self.price = input("Enter Price: ")
              price= str(self.price)  
              File.write(Id +', ' + product + ', '+ price + "\n")
      except Exception as e:
        print("Error: " + str(e))

    @staticmethod
    def ReadAllFileData(self, Message="Contents of File"):
      try:
        print(Message)
        self.seek(0)       # --> look for invenotry
        print(self.read()) # --> read the inventory 
      except Exception as e:
        print("Error: " + str(e))


###################################################################################


def main():
    #I/O
    # Provide path and name of file to work with
    File = input("what is the file name and path for your inventory?: ")
    print()
    
    
    # process new inventory
    try:
      # Read Invenotry
      f = Inventory(File)  
      objFile = open(File, "r+")
      f.ReadAllFileData(objFile, "Here is the current data:\n")
      f.WriteProductUserInput(objFile)
      f.ReadAllFileData(objFile, "\nHere is the data that was saved:\n")
    except FileNotFoundError as e:
         print("Error: " + str(e)) 
         a = input(str("\nThe file and path specified do not exist. Would you like to create a new inventory under" + File +"? y/n): "))
         if(a.lower() == "y"):
            print()
    # create new invenotry
            f = Inventory(File)       
            objFile = open(File, "w+")
            f.ReadAllFileData(objFile, "Here is the current data:")
            f.WriteProductUserInput(objFile)
            f.ReadAllFileData(objFile, "Here is the data that was saved\n")
         else:
            print("Ok - see you next time")
    except Exception as e:
        print("Error: " + str(e))
    #finally:
     # if(objFile != None):objFile.close()

main()
