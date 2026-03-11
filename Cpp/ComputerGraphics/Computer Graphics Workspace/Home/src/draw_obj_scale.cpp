#include <graphics.h>
#include <conio.h>

void drawTriangle(int x[], int y[], int color) {
    setcolor(color);
    line(x[0], y[0], x[1], y[1]);
    line(x[1], y[1], x[2], y[2]);
    line(x[2], y[2], x[0], y[0]);
}

void scaleTriangle(int x[], int y[], float sx, float sy, int scaledX[], int scaledY[], int cx, int cy) {
    for (int i = 0; i < 3; i++) {
        scaledX[i] = cx + (x[i] - cx) * sx;
        scaledY[i] = cy + (y[i] - cy) * sy;
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Original triangle vertices
    int x[3] = {200, 250, 150};
    int y[3] = {200, 300, 300};

    // Center of scaling (you can also use the centroid)
    int cx = 200, cy = 267;

    // Scaling factors
    float sx = 1.5;  // Zoom in (use <1.0 for zoom out)
    float sy = 1.5;

    // Arrays to store new scaled coordinates
    int scaledX[3], scaledY[3];

    // Draw original triangle in RED
    drawTriangle(x, y, RED);

    // Perform scaling
    scaleTriangle(x, y, sx, sy, scaledX, scaledY, cx, cy);

    // Draw scaled triangle in GREEN
    drawTriangle(scaledX, scaledY, GREEN);

    outtextxy(10, 10, "Red: Original, Green: Scaled");

    getch();
    closegraph();
    return 0;
}
