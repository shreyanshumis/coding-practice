#include <graphics.h>
#include <conio.h>
#include <iostream>

using namespace std;

void drawLineBresenham(int x0, int y0, int x1, int y1) {
    int dx = x1 - x0;
    int dy = y1 - y0;
    int p = 2 * dy - dx; // Initial decision parameter

    int x = x0, y = y0;

    // Plot first point
    putpixel(x, y, WHITE);

    while (x < x1) {
        x++;

        // Decision parameter determines next point
        if (p < 0) {
            p += 2 * dy;
        } else {
            y++;
            p += 2 * dy - 2 * dx;
        }

        putpixel(x, y, WHITE);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    // Fixed Starting and Ending Points
    int x0 = 100, y0 = 100;
    int x1 = 300, y1 = 200;

    drawLineBresenham(x0, y0, x1, y1);

    getch(); // Wait for key press
    closegraph();

    return 0;
}
