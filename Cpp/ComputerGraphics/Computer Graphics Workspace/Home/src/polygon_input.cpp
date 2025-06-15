#include <graphics.h>
#include <iostream>

using namespace std;

void drawAndFillPolygon(int points[][2], int n, int borderColor, int fillColor) {
    setcolor(borderColor);

    for (int i = 0; i < n - 1; i++) {
        line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1]);
    }
    line(points[n - 1][0], points[n - 1][1], points[0][0], points[0][1]); // Close polygon

    setfillstyle(SOLID_FILL, fillColor);

    int fillX = (points[0][0] + points[1][0]) / 2;
    int fillY = (points[0][1] + points[1][1]) / 2;

    floodfill(fillX, fillY, borderColor);
}

int main() {
    int n;

    cout << "Enter the number of vertices for the convex polygon: ";
    cin >> n;
    int convex[n][2];
    cout << "Enter the coordinates (x y) of the convex polygon:\n";
    for (int i = 0; i < n; i++) {
        cin >> convex[i][0] >> convex[i][1];
    }

    cout << "Enter the number of vertices for the concave polygon: ";
    cin >> n;
    int concave[n][2];
    cout << "Enter the coordinates (x y) of the concave polygon:\n";
    for (int i = 0; i < n; i++) {
        cin >> concave[i][0] >> concave[i][1];
    }

    cout << "Enter the number of vertices for the self-intersecting polygon: ";
    cin >> n;
    int selfIntersect[n][2];
    cout << "Enter the coordinates (x y) of the self-intersecting polygon:\n";
    for (int i = 0; i < n; i++) {
        cin >> selfIntersect[i][0] >> selfIntersect[i][1];
    }

    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    drawAndFillPolygon(convex, n, YELLOW, LIGHTBLUE);
    outtextxy(convex[0][0], convex[0][1] - 20, "Convex Polygon");

    drawAndFillPolygon(concave, n, GREEN, LIGHTRED);
    outtextxy(concave[0][0], concave[0][1] - 20, "Concave Polygon");

    drawAndFillPolygon(selfIntersect, n, RED, LIGHTGREEN);
    outtextxy(selfIntersect[0][0], selfIntersect[0][1] - 20, "Self-Intersecting Polygon");

    getch();
    closegraph();
    return 0;
}
