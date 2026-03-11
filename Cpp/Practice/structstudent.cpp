#include <iostream>
using namespace std;

typedef struct student //Takes up more memory than an union
{
    /* data */
    int Roll; //Roll no. of a student
    string language; //Language spoken by the student
    float Percentile; //Percentile of the student
} st;

union ptmoney //Pocket money and other tangible assets // Union does better data management than structure
{ //NOTE - Use only one at a time, not all 3 -
    int rupees; //currency
    char item; //items u have which have a value attached to them.
    float kgitem; //items but in kilograms
};

int main(){
    enum Meal{ breakfast, lunch, dinner}; //It stores 0 in breakfast, 1 in lunch and so on... increasing readability
    union ptmoney anshu;
    anshu.rupees=69;
    cout<<"Union\n"<<anshu.rupees<<endl;
    struct student shrey;
    //st shrey; also works(type typedef before struct)
    shrey.Roll = 30;
    shrey.language = "Odia";
    shrey.Percentile = 101.69420;
    cout<<"Structure\n";
    cout<<"The Roll Number is - "<<shrey.Roll<<endl;
    cout<<"The Language is - "<<shrey.language<<endl;
    cout<<"The Percentile is - "<<shrey.Percentile<<endl;
    return 0;
}