#include <graphics.h>
#include <conio.h>
#include <stdio.h>
void setTextAttributes(int font, int direction, int size) {
    settextstyle(font, direction, size);}
int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    setTextAttributes(TRIPLEX_FONT, HORIZ_DIR, 2);
    outtextxy(100, 100, "Shreyanshu in a simple font");
    setTextAttributes(TRIPLEX_FONT, HORIZ_DIR, 4);
    outtextxy(400, 200, "Bold Text");
    setTextAttributes(SIMPLEX_FONT, VERT_DIR, 3);
    outtextxy(200, 100, "Not bold or horizontal text");
    getch();
    closegraph();
    return 0;}