#include <iostream>
using namespace std;
class Employee
{
    private:
    string name;
    int age, id;
    public:
    Employee(string n, int a, int i)
    {
        name = n;
        age = a;
        id = i;
    }
    void show()
    {
        cout<<"Name:"<<name<<endl;
        cout<<"Age:"<<age<<endl;
        cout<<"ID:"<<id<<endl;
    }
};
//==================================================
class Qualification
{
    private:
    string degree;
    public:
    Qualification(string d)
    {
        degree=d;
    }
    void show()
    {
        cout<<"Degree:"<<degree<<endl;
    }
};
//==================================================
class Scientist:virtual public Employee, virtual public Qualification
{
    int vop;
    public:
    Scientist(string a, int b, int c, string d, int n): 
    Employee(a,b,c),
    Qualification(d)
    {
        cout<<"Scientist"<<endl;
    }

};
//==================================================
class Manager
{

};
//==================================================