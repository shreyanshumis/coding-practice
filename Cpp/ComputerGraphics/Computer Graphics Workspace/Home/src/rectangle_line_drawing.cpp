#include <graphics.h>
#include <conio.h>

// Function to draw a line using Bresenham's line algorithm
void drawLine(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1, dy = y2 - y1;
    int p = 2 * dy - dx;
    int twoDy = 2 * dy, twoDyDx = 2 * (dy - dx);
    int x = x1, y = y1;

    // If the line is horizontal (x1 == x2)
    if (dx == 0) {
        while (y != y2) {
            putpixel(x, y, WHITE);
            y += (dy > 0) ? 1 : -1;
        }
        return;
    }

    // If the line is vertical (y1 == y2)
    if (dy == 0) {
        while (x != x2) {
            putpixel(x, y, WHITE);
            x += (dx > 0) ? 1 : -1;
        }
        return;
    }

    // If the slope is less than 1 (shallow line)
    if (dx > dy) {
        putpixel(x, y, WHITE);  // plot initial point
        while (x < x2) {
            x++;
            if (p < 0)
                p += twoDy;
            else {
                y += (dy > 0) ? 1 : -1;
                p += twoDyDx;
            }
            putpixel(x, y, WHITE);
        }
    } else {  // If the slope is greater than 1 (steep line)
        putpixel(x, y, WHITE);  // plot initial point
        while (y < y2) {
            y++;
            if (p <= 0)
                p += twoDy;
            else {
                x += (dx > 0) ? 1 : -1;
                p += twoDyDx;
            }
            putpixel(x, y, WHITE);
        }
    }
}

// Function to draw a rectangle using the line algorithm
void drawRectangle(int x1, int y1, int x2, int y2) {
    // Draw four sides of the rectangle
    drawLine(x1, y1, x2, y1);  // Top side
    drawLine(x2, y1, x2, y2);  // Right side
    drawLine(x2, y2, x1, y2);  // Bottom side
    drawLine(x1, y2, x1, y1);  // Left side
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Define the coordinates of the rectangle
    int x1 = 100, y1 = 100, x2 = 300, y2 = 200;

    // Draw the rectangle
    drawRectangle(x1, y1, x2, y2);

    // Wait for a key press
    getch();
    closegraph();
    return 0;
}
