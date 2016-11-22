#Data
objFile = None #File Handle
strUserInput = None #A string which holds user input


#Processing
def WriteProductUserInput(File):
  try:
    print("Type in a Product Id, Name, and Price you want to add to the file")
    print("(Enter 'Exit' to quit!)")
    while(True):
      strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
      if(strUserInput.lower() == "exit"): break
      else: File.write(strUserInput + "\n")
  except Exception as e:
    print("Error: " + str(e))

def ReadAllFileData(File, Message="Contents of File"):
  try:
    print(Message)
    File.seek(0)
    print(File.read())
  except Exception as e:
    print("Error: " + str(e))


    #WriteProductUserInput("Products.txt")

# Provide path and name of file to work with

File = input(str("what is the file name and path for oyur inventory?: "))
print()

#I/O
try:
  objFile = open(File, "r+")
  ReadAllFileData(objFile, "Here is the current data:")
  WriteProductUserInput(objFile)
  ReadAllFileData(objFile, "Here is this data was saved:")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(objFile != None):objFile.close()
