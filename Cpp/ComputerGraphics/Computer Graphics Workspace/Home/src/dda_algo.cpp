
#include <graphics.h>
#include <cmath>
#include <iostream>

using namespace std;

void drawLineDDA(int x1, int y1, int x2, int y2) {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL); // Initialize graphics mode

    // Calculate dx and dy
    int dx = x2 - x1;
    int dy = y2 - y1;

    // Calculate the number of steps
    int steps = max(abs(dx), abs(dy));

    // Calculate increment values
    float x_inc = dx / (float)steps;
    float y_inc = dy / (float)steps;

    // Starting point
    float x = x1, y = y1;

    // Draw the line
    for (int i = 0; i <= steps; i++) {
        putpixel(round(x), round(y), WHITE);
        x += x_inc;
        y += y_inc;
        delay(10); // Slow down visualization
    }

    // Hold the screen
    getch();
    closegraph();
}

int main() {
    // Assume some fixed points
    int x1 = 100, y1 = 100;
    int x2 = 400, y2 = 300;

    drawLineDDA(x1, y1, x2, y2);

    return 0;
}
