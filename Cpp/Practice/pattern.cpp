#include <iostream>
using namespace std;

int main() {
    int rows = 4; //This is the no. of rows you'll have in ur pattern...
    for (int i = 0; i < rows; i++) { //This is the first loop, which will iterate for 4 times, going from the line 1 to 4
        for (int j = 0; j < rows - i; j++) {
        /*This is the second loop, which is responsible for the pattern of decreasing stars-- as you can see..i in the previous loop increments by one every time it goes to the next line, so subtracting the row with i will reduce row from 4 to 1 with every new iteration of i(it goes to the next line) */
            cout << "+ ";
        }
        cout<<endl;//this is a manipulator which helps u go to the next line
    }
    return 0;
}
