#include <graphics.h>
#include <conio.h>
#include <math.h>

// Function to draw a simple star
void drawStar(int centerX, int centerY, int radius) {
    int points[10];
    for (int i = 0; i < 5; ++i) {
        points[2*i] = centerX + radius * cos(2 * M_PI * i / 5);
        points[2*i+1] = centerY + radius * sin(2 * M_PI * i / 5);
    }
    for (int i = 0; i < 5; ++i) {
        int next = (i + 2) % 5;
        line(points[2*i], points[2*i+1], points[2*next], points[2*next+1]);
    }
}

// Function to draw a plus sign
void drawPlus(int centerX, int centerY, int size) {
    line(centerX - size, centerY, centerX + size, centerY); // Horizontal
    line(centerX, centerY - size, centerX, centerY + size); // Vertical
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Draw horizontal line
    line(100, 100, 300, 100);

    // Draw vertical line
    line(200, 150, 200, 300);

    // Draw star
    drawStar(400, 150, 50);

    // Draw plus sign
    drawPlus(400, 300, 30);

    getch();
    closegraph();
    return 0;
}
