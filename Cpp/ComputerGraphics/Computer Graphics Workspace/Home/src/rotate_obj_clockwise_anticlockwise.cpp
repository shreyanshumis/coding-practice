#include <graphics.h>
#include <conio.h>
#include <math.h>

#define PI 3.14159265

void drawTriangle(int x[], int y[], int color) {
    setcolor(color);
    line(x[0], y[0], x[1], y[1]);
    line(x[1], y[1], x[2], y[2]);
    line(x[2], y[2], x[0], y[0]);
}

void rotateTriangle(int x[], int y[], int xr[], int yr[], float angle, int cx, int cy) {
    float rad = angle * PI / 180;
    for (int i = 0; i < 3; i++) {
        // Translate point to origin
        int tx = x[i] - cx;
        int ty = y[i] - cy;
        // Apply rotation
        xr[i] = cx + (int)(tx * cos(rad) - ty * sin(rad));
        yr[i] = cy + (int)(tx * sin(rad) + ty * cos(rad));
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Original triangle coordinates
    int x[3] = {200, 250, 150};
    int y[3] = {200, 300, 300};

    // Rotation pivot (centroid)
    int cx = (x[0] + x[1] + x[2]) / 3;
    int cy = (y[0] + y[1] + y[2]) / 3;

    // Arrays to hold rotated coordinates
    int xCW[3], yCW[3];    // Clockwise
    int xACW[3], yACW[3];  // Anticlockwise

    // Rotation angle (degrees)
    float angle = 45;

    // Rotate clockwise (positive angle)
    rotateTriangle(x, y, xCW, yCW, angle, cx, cy);

    // Rotate anticlockwise (negative angle)
    rotateTriangle(x, y, xACW, yACW, -angle, cx, cy);

    // Draw original in RED
    drawTriangle(x, y, RED);
    outtextxy(10, 10, "Red: Original");

    // Draw clockwise rotated in GREEN
    drawTriangle(xCW, yCW, GREEN);
    outtextxy(10, 25, "Green: Rotated Clockwise");

    // Draw anticlockwise rotated in BLUE
    drawTriangle(xACW, yACW, BLUE);
    outtextxy(10, 40, "Blue: Rotated Anticlockwise");

    getch();
    closegraph();
    return 0;
}
