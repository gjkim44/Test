using System;

class Program
{
    static void Main(string[] args)
    {
        Employee objE1 = new Employee();
        objE1.Id = 1;
        objE1.FirstName = "Bob";
        EmployeeList.AddEmployee(objE1);

        Employee objE2 = new Employee(2, "Sue");
        EmployeeList.AddEmployee(objE2);

        Console.WriteLine(EmployeeList.ToString());
        Console.ReadLine();
    }
}

