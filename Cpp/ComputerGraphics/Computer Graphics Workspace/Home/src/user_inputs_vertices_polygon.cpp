#include <graphics.h>
#include <conio.h>
#include <stdio.h>

int main() {
    int n = 5;  // Hardcoded number of vertices (example: 5 vertices)
    int i;

    int points[2 * n + 2]; // Extra for closing polygon

    // Hardcoded vertices (you can change these as needed)
    int vertices[5][2] = {
        {100, 100},
        {200, 50},
        {300, 150},
        {250, 250},
        {150, 200}
    };

    // Copy hardcoded values to the points array
    for (i = 0; i < n; i++) {
        points[2 * i] = vertices[i][0];
        points[2 * i + 1] = vertices[i][1];
    }

    // Repeat first point to close the polygon
    points[2 * n] = points[0];
    points[2 * n + 1] = points[1];

    // Graphics initialization
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);  //  NULL instead of ""

    cleardevice();

    setcolor(WHITE);
    drawpoly(n + 1, points);  // Draw polygon

    setfillstyle(SOLID_FILL, CYAN);

    // Attempt floodfill inside polygon
    floodfill(points[0] + 10, points[1] + 10, WHITE); //  More reliable

    outtextxy(10, 10, "User-defined Polygon");

    getch();
    closegraph();
    return 0;
}
