#include <iostream>
using namespace std;
int main()
{
    float mh = 448;
    float ka = 236;
    float tn = 311;
    float up = 240;

    float mhg =12.0;
    float upg =17.1;
    float kag =9.5;
    float tng =14.6;

    int y=0;

    while (mh < 1000 && ka < 1000 && tn < 1000 && up < 1000)
    {
        up=up*(1+upg/100);
        ka=ka*(1+kag/100);
        mh=mh*(1+mhg/100);
        tn=tn*(1+tng/100);
        y+=1;
    }
    cout <<"UP:"<<up<<"\nMH:"<<mh<<"\nKA:"<<ka<<"\nTN"<<tn<<endl;
    cout <<y;
    
}