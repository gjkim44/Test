class Person
{
    //--Fields--
    static int __Counter = 0; 
    string __FirstName;

    //--Constructor--
    public Person(string FirstName = "")
    {
        //Attributes
        this.__FirstName = FirstName; // Private Attribute = Field in C#
        Person.__SetObjectCount(); // Private Static Method
    }

    //--Properties--
    //FirstName    
    public string FirstName
    {
        get
        { return __FirstName; }
        set
        { __FirstName = value; }
    }

    public override string ToString()
    {
        return this.FirstName;
    }

    static int GetObjectCount()
    { // You do not need the self keyword
        return Person.__Counter;
    }

    static void __SetObjectCount()
    { // This is a private and static method
        Person.__Counter += 1;
    }
}//--End of class Person--
