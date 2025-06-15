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

void rotateAboutPoint(int x[], int y[], int xr[], int yr[], float angle, int px, int py) {
    float rad = angle * PI / 180;
    for (int i = 0; i < 3; i++) {
        int tx = x[i] - px;
        int ty = y[i] - py;
        xr[i] = round(px + tx * cos(rad) - ty * sin(rad));
        yr[i] = round(py + tx * sin(rad) + ty * cos(rad));
    }
}

void translateTriangle(int x[], int y[], int dx, int dy) {
    for (int i = 0; i < 3; i++) {
        x[i] += dx;
        y[i] += dy;
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Original triangle (more central)
    int x[3] = {200, 250, 150};
    int y[3] = {200, 300, 300};

    float angle = 45;

    int xOrigin[3], yOrigin[3];
    int xFixed[3], yFixed[3];

    // Rotate about origin
    rotateAboutPoint(x, y, xOrigin, yOrigin, angle, 0, 0);

    // Translate rotated-origin triangle into view (move right and down)
    translateTriangle(xOrigin, yOrigin, 200, 100);

    // Rotate about centroid
    int cx = (x[0] + x[1] + x[2]) / 3;
    int cy = (y[0] + y[1] + y[2]) / 3;
    rotateAboutPoint(x, y, xFixed, yFixed, angle, cx, cy);

    // Draw triangles
    drawTriangle(x, y, RED);             // Original
    drawTriangle(xOrigin, yOrigin, GREEN); // Rotated about origin (and moved into view)
    drawTriangle(xFixed, yFixed, BLUE);  // Rotated about centroid

    // Labels
    setcolor(RED);
    outtextxy(10, 10, "Red: Original");
    setcolor(GREEN);
    outtextxy(10, 30, "Green: Rotated about Origin (translated)");
    setcolor(BLUE);
    outtextxy(10, 50, "Blue: Rotated about Centroid");

    getch();
    closegraph();
    return 0;
}
