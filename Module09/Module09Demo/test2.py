if __name__ == "__main__":
    import Employees
else:
    raise Exception("This file was not created to be imported ")

objE = Employees.Employee()
objE.Id = 1
objE.FirstName = "Bob"

print(objE.ToString())

print(Employees.Employee.AddEmployee(objE))