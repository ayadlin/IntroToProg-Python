#------------Customers.py ---------------#
#Desc:  Class that hold Customers
#Dev:   ayadlin
#Date:  11/30/16
#ChangeLog:Modified from RRoot Employees class
#---------------------------------------------#
import Persons, Contacts

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")

#--- Make child class ---
class Customer(Contacts.Contact):
    """ Class for Customer data """
    
    #--Fields--
    #Id = Customer Id
    #CC = Credit Card
    #ED = Expiration Date
    #CVC = Security Code

    
#--Constructor--
    def __init__(self, Id = "", CC = 0000000000000000, ED =0000, CVC= 000):
        #Attributes
        self.__Id = Id
        self.__CC = CC
        self.__ED = ED
        self.__CVC = CVC

    #--Properties--
    # Id    
    @property #getter(accessor) 
    def Id(self):
        return self.__Id
    
    @Id.setter #(mutator)
    def Id(self, Value):
        self.__Id = Value

    # CC    
    @property #getter(accessor) 
    def CC(self):
        if len(str(self.__CC))== 16 and isinstance(self.__CC,int):
            return self.__CC
        else:
            cc = input("Enter correct 16 digit credit card number: " )
            self.__CC = cc
            return self.__CC
        
            
    @CC.setter #(mutator)
    def CC(self, Value):
        if len(str(Value)) == 16 and isinstance(Value,int):
            self.__CC = Value
        else:
            cc = input("Enter correct 16 digit credit card number: " )
            self.__CC = cc
            
    # ED    
    @property #getter(accessor) 
    def ED(self):
        if len(str(self.__ED)) == 4 and isinstance(self.__ED,int):
            return self.__ED
        else:
            ed = input("Enter correct 4 digit expiration date: " )
            self.__ED = ed
            return self.__ED
        
            
    @ED.setter #(mutator)
    def ED(self, Value):
        if len(str(Value)) == 4 and isinstance(Value,int):
            self.__ED = Value
        else:
            ed = input("Enter correct 4 digit expiration date: " )
            self.__ED = ed

    # CVC    
    @property #getter(accessor) 
    def CVC(self):
        if 2 < len(str(self.__CVC)) < 5 and isinstance(self.__CVC,int):
            return self.__CVC
        else:
            cvc = input("Enter correct 3/4 digit security code: " )
            self.__CVC = cvc
            return self.__CVC
        
            
    @CVC.setter #(mutator)
    def CVC(self, Value):
        if 2 < len(str(Value)) < 5 and isinstance(Value,int):
            self.__CVC = Value
        else:
            cvc = input("Enter correct 3/4 digit security code: " )
            self.__CVC = cvc    
    
    #--Methods--

    def ToString(self): 
        """Explictly returns field data"""
        strData = super().ToString()
        return str(self.Id) + ',' + strData
    
    def __str__(self):
        """Implictly returns field data"""
        return self.ToString()   

#--End of Class Customer --         


class CustomerList(object):
    """ Static class for holding a list of Employee data """
    #-------------------------------------#
    #Desc:  Manages a list of Customer data
    #Dev:   ayadlin 
    #Date:  11/30/2016
    #ChangeLog:adapted from Rroot EmployeeList
    #-------------------------------------#
    
    #--Fields--
    __lstCustomers = [] # a list with Employee objects

    #--Constructor--
    #@staticmethod in python constructors cannot be static 
    #def __init__():
        #Attributes
       
    #--Properties--
        #None

    # QUESTION:
    # If we can not make static constructors
    # is there other way to name the list so we end we several list
    # ie TARGET costumers, Amazon Costumers etc - from the CustomerList Class?
    # THANKS

    
    #--Methods--      
    @staticmethod            
    def AddCustomer(Customer):
        #print(Customer.__class__)#for testing
        if(str(Customer.__class__) == "<class 'Customers.Customer'>"):
            CustomerList.__lstCustomers.append(Customer)
            #print(CustomerList.__lstCustomers)#for testing
        else:
            raise Exception("Only Customer objects can be added to this list")
         
    @staticmethod           
    def ToString(): # This overrides the original method (it's polymorphic)
        """Explictly returns field data"""
        strData = "" # "Id, FirstName, LastName, Number, Street, App, Zip, Phone, E-mail"\
        #          " Credit Card #, Exp. Date, Security Code \n" # will move this to main
        for item in CustomerList.__lstCustomers:
            strData += str(item.Id) + ", " + item.FirstName + ", " + item.LastName + ", " +\
                       str(item.Nu) + " " + item.St + " " + item.App + ", " + item.ZipC + \
                       ", " + str(item.Ph) + ", " + item.Em + ", " + str(item.CC) + ", " + \
                       str(item.ED) + ", " + str(item.CVC) + "\n"
        return strData
    
    @staticmethod
    def __str__(): # This overrides the original method as well
        """Implictly returns field data"""
        strData = CustomerList.ToString
        return strData        

#--End of Class CustomerList--
