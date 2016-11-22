#Data
objFile = None #File Handle
strUserInput = None #A string which holds user input

# The first class creates a new inventory obeject/reads it
class Inventory(object):

    # Create new inventory
    def __init__(self,name):
        self.name = name

# The second class process the new inventory object

class Processing():     
    @staticmethod    
    def WriteProductUserInput(File):
      try:
        print("Type in a Product Id, Name, and Price you want to add to the file")
        print("(Enter 'Exit' to quit!)\n")
        while(True):
          strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
          if(strUserInput.lower() == "exit"): break
          else: File.write(strUserInput + "\n")
      except Exception as e:
        print("Error: " + str(e))

    @staticmethod
    def ReadAllFileData(File, Message="Contents of File"):
      try:
        print(Message)
        File.seek(0)
        print(File.read())
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
      Processing.ReadAllFileData(objFile, "Here is the current data:\n")
      Processing.WriteProductUserInput(objFile)
      Processing.ReadAllFileData(objFile, "\nHere is this data was saved:\n")
    except FileNotFoundError as e:
         print("Error: " + str(e) + "\n Please check the file name")
         a = input(str("\n Would you like to create a new inventory under that name? y/n): "))
         if(a.lower() == "y"):
            print()
    # create new invenotry
            f = Inventory(File)       
            objFile = open(File, "w+")
            Processing.ReadAllFileData(objFile, "Here is the current data:")
            Processing.WriteProductUserInput(objFile)
            Processing.ReadAllFileData(objFile, "Here is this data was saved:n")
         else:
            print("Ok - see you next time")
    except Exception as e:
        print("Error: " + str(e))
    #finally:
     # if(objFile != None):objFile.close()

main()
