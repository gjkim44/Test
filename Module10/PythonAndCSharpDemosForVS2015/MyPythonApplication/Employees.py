import Persons

#--- Make child class ---
class Employee(Persons.Person):
    """ Class for Employee data """
    #-------------------------------------#
    #Desc:  Holds Employee data
    #Dev:   RRoot 
    #Date:  12/12/2020
    #ChangeLog:(When,Who,What)
    #-------------------------------------#
    
    #--Fields--
    #Id = Employee Id
    
#--Constructor--
    def __init__(self, Id = "", FirstName = ""):
        #Attributes
        self.__Id = Id
        self.FirstName = FirstName

    #--Properties--
    # Id    
    @property #getter(accessor) 
    def Id(self):
        return self.__Id
    
    @Id.setter #(mutator)
    def Id(self, Value):
        self.__Id = Value
    
    #--Methods--
    def ToString(self):
        """Explictly returns field data"""
        strData = super().ToString()
        return str(self.Id) + ',' + strData
    
    def __str__(self):
        """Implictly returns field data"""
        return self.ToString()   
#--End of Class Employee --         

class EmployeeList(object):
    """ Static class for holding a list of Employee data """
    #-------------------------------------#
    #Desc:  Manages a list of Employee data
    #Dev:   RRoot
    #Date:  12/12/2020
    #ChangeLog:(When,Who,What)
    #-------------------------------------#

    #--Fields--
    __lstEmployees = [] # a list with Employee objects

    #--Constructor--
    #@staticmethod in python constructors cannot be static
    #def __init__():
        #Attributes

    #--Properties--
        #None

    #--Methods--
    @staticmethod
    def AddEmployee(Employee):
        if(str(Employee.__class__) == "<class 'Employees.Employee'>"):
            EmployeeList.__lstEmployees.append(Employee)
        else:
            raise Exception("Only Employee objects can be added to this list")

    @staticmethod
    def ToString(): # This overrides the original method (it's polymorphic)
        """Explictly returns field data"""
        strData = "Id,FirstName\n"
        for item in EmployeeList.__lstEmployees:
            strData += str(item.Id) + "," + item.FirstName + "\n"
        return strData

    @staticmethod
    def __str__(): # This overrides the original method as well
        """Implictly returns field data"""
        strData = EmployeeList.ToString
        return strData
#--End of Class --
