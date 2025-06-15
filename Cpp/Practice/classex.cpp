#include <iostream>
#include <string>
using namespace std;

class Employee
{
    private:
        string name, game, ytname;
    public:
        void setData(string a1, string b1, string c1); 
        void getData(){
            cout<<"Your name: "<<name<<endl;
            cout<<"Your favourite game: "<<game<<endl;
            cout<<"Your favourite youtube channel: "<<ytname<<endl;
        }
};

void Employee :: setData(string a1, string b1, string c1){
    name = a1;
    game = b1;
    ytname = c1;
}
int main(){
    Employee shrey;
    string x,y,z;
    cout<<"Enter your name, favourite game and favourite youtube channel"<<endl;
    cin>>x;
    cin>>y;
    cin>>z;
    shrey.setData(x,y,z);
    shrey.getData();
    return 0;
}
