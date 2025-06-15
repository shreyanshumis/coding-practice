#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main()
{
    srand(time(0));
    int runs = 0;
    int i;
    i = (rand() % 100) + 1;
    cout<<"Welcome to Batting simulator"<<endl;
    cout<<"Enter your name :"<<endl;
    string name;
    cin>>name;
    cout << "Your winning score " << i << "\n";
    while (1) {
        int user1 = 0;
        int a;
        if (runs > i) {
            cout << "You won!! \nTotal Runs scored:"
                 << runs << "\n";
            exit(0);
        }
        else {
            a = (rand() % 6) + 0;
            cout << "Enter no. between 0 and 6" << endl;
            cin >> user1;
            cout << "Computer : " << a << endl;
            if (user1 == a) {
                cout << "Bowled!! \nTotal Runs scored:"
                     << runs
                     << endl;
                exit(0);
            }
            else {
                runs = runs + user1;
                cout << "Runs scored by "<<name<<" : "<<runs<<endl; 
            }
        }
    }
  
    return 0;
}