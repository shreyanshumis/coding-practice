#include <graphics.h>
#include <iostream>

using namespace std;

// Function to draw a polygon given an array of points
void drawPolygon(int points[][2], int n, int color) {
    setcolor(color);
    for (int i = 0; i < n - 1; i++) {
        line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1]);
    }
    line(points[n - 1][0], points[n - 1][1], points[0][0], points[0][1]); // Close the polygon
}

int main() {
    // Initialize graphics mode
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    // Get screen width and height
    int width = getmaxx();
    int height = getmaxy();
    int centerX = width / 2;

    // Convex Polygon (Hexagon) - Left side
    int convex[6][2] = {
        {centerX - 250, 100}, {centerX - 200, 150}, {centerX - 200, 200},
        {centerX - 250, 250}, {centerX - 300, 200}, {centerX - 300, 150}
    };
    drawPolygon(convex, 6, YELLOW);
    outtextxy(centerX - 280, 270, "Convex Polygon");

    // Concave Polygon (Arrow-like shape) - Center-left
    int concave[6][2] = {
        {centerX - 80, 100}, {centerX - 30, 150}, {centerX - 60, 180}, 
        {centerX - 30, 220}, {centerX - 80, 250}, {centerX - 130, 180}
    };
    drawPolygon(concave, 6, GREEN);
    outtextxy(centerX - 110, 270, "Concave Polygon");

    // Self-Intersecting Polygon (Bowtie shape) - Centered
    int selfIntersect[6][2] = {
        {centerX + 50, 120}, {centerX + 120, 200}, {centerX + 190, 120}, 
        {centerX + 190, 230}, {centerX + 120, 150}, {centerX + 50, 230}
    };
    drawPolygon(selfIntersect, 6, RED);
    outtextxy(centerX + 70, 270, "Self-Intersecting Polygon");

    // Hold the screen
    getch();
    closegraph();
    return 0;
}
