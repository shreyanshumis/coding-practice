#include <iostream>
using namespace std;

int main(){
    int a = 69;
    int* b= &a;
    cout<<"Address of 'a' is :"<<b<<endl;
    // & ====> (Address of) operator
    cout<<"The value of Adress b is :"<<*b<<endl;
    // * ====> (Value of) Dereference operator
    return 0;
}