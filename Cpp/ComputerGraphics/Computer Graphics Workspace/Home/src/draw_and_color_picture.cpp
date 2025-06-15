#include <graphics.h>
#include <conio.h>

void drawFace()
{
    int x = 250, y = 200, r = 100;
    setcolor(YELLOW);
    setfillstyle(SOLID_FILL, YELLOW);
    fillellipse(x, y, r, r);

    setcolor(BLACK);
    setfillstyle(SOLID_FILL, BLACK);
    fillellipse(x - 40, y - 30, 10, 15);
    fillellipse(x + 40, y - 30, 10, 15);

    arc(x, y, 200, 340, 50);
    line(x, y - 10, x, y + 20);
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    drawFace();
    getch();
    closegraph();
    return 0;
}