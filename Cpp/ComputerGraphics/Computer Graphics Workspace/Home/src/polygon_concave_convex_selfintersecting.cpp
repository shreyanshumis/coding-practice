#include <graphics.h>
#include <conio.h>

void drawConvexPolygon() {
    // Convex: all interior angles < 180 degrees
    int points[] = {100, 100, 150, 80, 200, 100, 180, 150, 120, 150, 100, 100};
    drawpoly(6, points); // 5 points + return to first point
    outtextxy(100, 160, "Convex Polygon");
}

void drawConcavePolygon() {
    // Concave: has at least one interior angle > 180 degrees
    int points[] = {300, 100, 350, 80, 400, 100, 370, 130, 330, 130, 360, 100, 300, 100};
    drawpoly(8, points); // 7 points + return
    outtextxy(300, 160, "Concave Polygon");
}

void drawSelfIntersectingPolygon() {
    // Self-intersecting (star-like shape)
    int points[] = {500, 100, 550, 150, 500, 150, 550, 100, 500, 100};
    drawpoly(6, points); // 5 points + return
    outtextxy(500, 160, "Self-Intersecting");
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    setcolor(WHITE);

    drawConvexPolygon();
    drawConcavePolygon();
    drawSelfIntersectingPolygon();

    getch();
    closegraph();
    return 0;
}
