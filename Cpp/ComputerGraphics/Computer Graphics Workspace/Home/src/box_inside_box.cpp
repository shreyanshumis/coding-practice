#include <graphics.h>
#include <conio.h>

int main() {
    int gd = DETECT, gm;

    // Initialize graphics mode
    initgraph(&gd, &gm, "");

    // Outer box coordinates
    int left1 = 100, top1 = 100, right1 = 300, bottom1 = 300;
    // Inner box coordinates (smaller and centered)
    int left2 = 150, top2 = 150, right2 = 250, bottom2 = 250;

    // Draw outer box
    rectangle(left1, top1, right1, bottom1);

    // Draw inner box
    rectangle(left2, top2, right2, bottom2);

    getch();  // Wait for key press
    closegraph();  // Close graphics mode

    return 0;
}
