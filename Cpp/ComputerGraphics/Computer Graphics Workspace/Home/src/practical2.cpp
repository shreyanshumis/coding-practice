#include <graphics.h>
#include <conio.h>
void drawCirclePoints(int xc, int yc, int x, int y) {
    putpixel(xc + x, yc + y, WHITE);
    putpixel(xc - x, yc + y, WHITE);
    putpixel(xc + x, yc - y, WHITE);
    putpixel(xc - x, yc - y, WHITE);
    putpixel(xc + y, yc + x, WHITE);
    putpixel(xc - y, yc + x, WHITE);
    putpixel(xc + y, yc - x, WHITE);
    putpixel(xc - y, yc - x, WHITE);}
    
void midpointCircle(int xc, int yc, int r) {
    int x = 0;
    int y = r;
    int p = 1 - r;
    drawCirclePoints(xc, yc, x, y);
    while (x < y) {
        x++;
        if (p < 0) {
            p = p + 2 * x + 1;
        } else {
            y--;
            p = p + 2 * (x - y) + 1;
        }
        drawCirclePoints(xc, yc, x, y);
    setcolor(RED);
    putpixel(xc, yc, RED);
    putpixel(xc - 1, yc, RED);
    putpixel(xc + 1, yc, RED);
    putpixel(xc, yc - 1, RED);   
    putpixel(xc, yc + 1, RED);
}}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    midpointCircle(250, 200, 100); 
    getch();
    closegraph();
    return 0;}

