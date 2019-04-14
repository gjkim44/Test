class Employee : Person
{

    //--Fields--
    int __Id;

    //--Constructor--
    public Employee(int Id = 0, string FirstName = "")
    {   // Attributes
        this.__Id = Id;
        this.FirstName = FirstName;
    }

    //--Properties--
    public int Id
    {
        get { return __Id; }
        set { __Id = value; }
    }

    //--Methods--
    public override string ToString()
    {
        string strData = base.ToString();
        return Id.ToString() + ',' + strData;
    }
} //--End of Class Employee --   


class EmployeeList : object
{
    //--Fields--
    static System.Collections.Generic.List<Employee> __lstEmployees;// a list with Employee objects

    //--Constructor--
    //@staticmethod in python constructors cannot be static
    static EmployeeList()
    {
        __lstEmployees = new System.Collections.Generic.List<Employee>();
    }

    //--Properties--
    public static System.Collections.Generic.List<Employee> LstEmployees
    {
        get { return __lstEmployees; }
        set { __lstEmployees = value; }
    }
    //--Methods--

    public static void AddEmployee(Employee NewEmployee)
    {
        EmployeeList.__lstEmployees.Add(NewEmployee);
    }

    public static new string ToString()
    { // This overrides the original method (it's polymorphic)
        string strData = "Id,FirstName\n";
        foreach (var item in EmployeeList.__lstEmployees)
        {
            strData += (item.Id).ToString() + "," + item.FirstName + "\n";
        }
        return strData;
    }
}//--End of Class --