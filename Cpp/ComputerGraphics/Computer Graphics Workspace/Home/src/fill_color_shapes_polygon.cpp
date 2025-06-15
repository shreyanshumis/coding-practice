#include <graphics.h>
#include <conio.h>

void drawConvexPolygon() {
    int points[] = {100, 100, 150, 80, 200, 100, 180, 150, 120, 150, 100, 100};
    drawpoly(6, points);
    setfillstyle(SOLID_FILL, GREEN);
    floodfill(150, 110, WHITE);
    outtextxy(100, 160, "Convex Polygon");
}

void drawConcavePolygon() {
    int points[] = {300, 100, 350, 80, 400, 100, 370, 130, 330, 130, 360, 100, 300, 100};
    drawpoly(8, points);
    setfillstyle(SOLID_FILL, CYAN);
    floodfill(350, 105, WHITE);  // Ensure this point is **within** the closed part
    outtextxy(300, 160, "Concave Polygon");
}

void drawSelfIntersectingPolygon() {
    int points[] = {500, 100, 550, 150, 500, 150, 550, 100, 500, 100};
    drawpoly(6, points);
    setfillstyle(SOLID_FILL, YELLOW);
    floodfill(510, 110, WHITE);  // Try top triangle section
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
