#include<iostream>
#include<string>
using namespace std;

class Car {
    int gear,speed;
    string color;

    public:
        Car (string color) {
            this->color = color;
            this->gear = 0;
            this->speed = 0;
        }
    void changeGear(int up=1)
    {
        if(up==1){
            this->gear = ++(this->gear);
        }
        else {
            this->gear = --(this->gear);       
        }
        cout<<"\nCurrent Gear : "<<(this->gear); 
    }

    void accelerate() {
        this->speed += 10;
            cout<<"\nCurrent Speed : "<<(this->speed); 

    }

    void brake() {
        this->speed = 0;
    }
};

class SuperCar: Car {
    
};

int main() {
    string clr;
    cout<<"What color car? : ";
    cin>>clr;
    Car car(clr);
    cout<<clr<<" Vroom.....";
    car.changeGear();
    car.accelerate();
}