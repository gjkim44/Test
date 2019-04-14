import Employees

objE1 = Employees.Employee()
objE1.Id = 1
objE1.FirstName = "Bob"
Employees.EmployeeList.AddEmployee(objE1)

objE2 = Employees.Employee(2,"Sue")
Employees.EmployeeList.AddEmployee(objE2)

print(Employees.EmployeeList.ToString())
input()