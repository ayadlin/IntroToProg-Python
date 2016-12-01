#------------Contacts.py ---------------#
#Desc:  Class that hold Contact data
#Dev:   ayadlin 
#Date:  11/30/16
#ChangeLog:Adapted from Employees.py by RRoot
#---------------------------------------------#
import Persons

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")

#--- Make child class ---
class Contact(Persons.Person):
    """ Class for Contact data """
    
    #--Fields--
    #St = Contact Street
    #Nu = Contact Street Number
    #App = Contact Appartment
    #ZipC = Contact Zip Code number
    #Ph = Contact Phone Number
    #Em = Contact E-mail address 
    
    
#--Constructor--
    def __init__(self, Nu = 0, St = "",  App = "n/a", ZipC = 00000,\
                 Ph = 0000000000, Em = ""):
        #Attributes
        self.__St = St
        self.__Nu = Nu
        self.__App = App
        self.__ZipC = ZipC
        self.__Ph = Ph
        self.__Em = Em

    #--Properties--

    # First the easier ones    

    # St
    @property #getter(accessor) 
    def St(self):
        return self.__St
        
    @St.setter #(mutator)
    def St(self, Value):
        self.__St = Value

    # App
    @property #getter(accessor) 
    def App(self):
        return self.__App
        
    @App.setter #(mutator)
    def App(self, Value):
        self.__App = Value    

    # Em
    @property #getter(accessor) 
    def Em(self):
        return self.__Em
        
    @Em.setter #(mutator)
    def Em(self, Value):
        self.__Em = Value

    # Now the more involved ones
    
    # Nu    
    @property #getter(accessor) 
    def Nu(self):
        if isinstance(self.__Nu,int):
            return self.__Nu
        else:
            nu = input("Enter correct house number: " )
            self.__Nu = nu
            return self.__Nu
        
            
    @Nu.setter #(mutator)
    def Nu(self, Value):
        if isinstance(Value,int):
            self.__Nu = Value
        else:
            nu = input("Enter correct house number: " )
            self.__Nu = nu
            
    # ZipC    
    @property #getter(accessor) 
    def ZipC(self):
        if len(self.__ZipC) == 5:
            return self.__ZipC   
        else:
            z = input("Enter correct 5 digit Zip code: " )
            self.__ZipC = z
            return self.__ZipC
        
            
    @ZipC.setter #(mutator)
    def ZipC(self, Value):
        if  len(Value) == 5 and isinstance(int(Value),int):
            self.__ZipC = Value
        else:
            z = input("Enter correct 5 digit Zip code: " )
            self.__ZipC = z

    # Ph    
    @property #getter(accessor) 
    def Ph(self):
        if 9 < len(str(self.__Ph)) < 12 and isinstance(self.__Ph,int):
            return self.__Ph
        else:
            ph = input("Enter correct phone number starting by country area code: " )
            self.__Ph = ph
            return self.__Ph    
        
            
    @Ph.setter #(mutator)
    def Ph(self, Value):
        if 9 < len(str(Value)) < 12 and isinstance(Value,int):
            self.__Ph = Value
        else:
            ph = input("Enter correct phone number starting by country area code: " )
            self.__Ph = ph    
    
    #--Methods--

    #Return phone and e-mail onley
    def ToString(self): 
        """Explictly returns field data"""
        strData = super().ToString()
        return strData + ',' + str(self.Ph) + ',' + str(self.Em) 
    
    def __str__(self):
        """Implictly returns field data"""
        return self.ToString()   
#--End of Class Contact --         

