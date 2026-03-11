#include <graphics.h>
#include <conio.h>
#include <math.h>

void DDA(int x1, int y1, int x2, int y2) {
    float dx = x2 - x1;
    float dy = y2 - y1;
    float steps = fabs(dx) > fabs(dy) ? fabs(dx) : fabs(dy);

    float xInc = dx / steps;
    float yInc = dy / steps;

    float x = x1;
    float y = y1;

    for (int i = 0; i <= steps; i++) {
        putpixel(round(x), round(y), WHITE);
        x += xInc;
        y += yInc;
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Line end points
    int x1 = 100, y1 = 100, x2 = 400, y2 = 300;

    // Call DDA line drawing
    DDA(x1, y1, x2, y2);

    getch();
    closegraph();
    return 0;
}
