#include <graphics.h>
#include <conio.h>
#include <math.h>

// Function to draw a circle using Bresenham's algorithm
void drawCircle(int x_center, int y_center, int radius) {
    int x = 0, y = radius;
    int p = 3 - 2 * radius;  // Initial decision parameter

    // Plot the initial points at the octant positions
    while (x <= y) {
        putpixel(x_center + x, y_center + y, WHITE);
        putpixel(x_center - x, y_center + y, WHITE);
        putpixel(x_center + x, y_center - y, WHITE);
        putpixel(x_center - x, y_center - y, WHITE);
        putpixel(x_center + y, y_center + x, WHITE);
        putpixel(x_center - y, y_center + x, WHITE);
        putpixel(x_center + y, y_center - x, WHITE);
        putpixel(x_center - y, y_center - x, WHITE);

        // Update the decision parameter and coordinates
        if (p <= 0) { 
            p = p + 4 * x + 6;
        } else {
            p = p + 4 * (x - y) + 10;
            y--;
        }
        x++;
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Set the center and radius for the circle
    int x_center = 320, y_center = 240, radius = 100;

    // Draw the circle using Bresenham's algorithm
    drawCircle(x_center, y_center, radius);

    // Wait for a key press
    getch();
    closegraph();
    return 0;
}
