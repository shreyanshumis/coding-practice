#include <graphics.h>
#include <conio.h>
#include <stdio.h>

void setTextAttributes(int font, int direction, int size) {
    settextstyle(font, direction, size);
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Horizontal text: Bold, Triplex, Size 2
    setTextAttributes(TRIPLEX_FONT, HORIZ_DIR, 2);
    outtextxy(100, 100, "Shreyyyyz");

    // Vertical text: Bold, Triplex, Size 4
    setTextAttributes(TRIPLEX_FONT, VERT_DIR, 4);
    outtextxy(50, 100, "Bold Text");

    // Another vertical example with different font
    setTextAttributes(SIMPLEX_FONT, VERT_DIR, 3);
    outtextxy(200, 100, "Simplex");

    getch();
    closegraph();
    return 0;
}
