#include <graphics.h>
#include <conio.h>

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Draw a circle
    // Syntax: circle(x_center, y_center, radius);
    circle(250, 200, 100);  // Draws a circle with center at (250, 200) and radius 100

    getch(); // Wait for a key press
    closegraph(); // Close graphics window
    return 0;
}

