if __name__ == "__main__":
    import DataProcessor, Employees, Persons
else:
    raise Exception("This file was not created to be imported ")

p1 = Persons.Person("Bob","Smith")
print(p1)

e1 = Employees.Employee(1, "Sue", "Jones")
print(e1)

Employees.EmployeeList.AddEmployee(e1)
print(Employees.EmployeeList.ToString())