#include <graphics.h>
#include <conio.h>

void draw3DBar(int left, int top, int right, int bottom, int depth) {
    // Front rectangle
    rectangle(left, top, right, bottom);

    // Points for 3D effect
    int rTopX = right, rTopY = top;
    int rBottomX = right, rBottomY = bottom;
    int offsetX = depth, offsetY = -depth;

    // Draw side edges for 3D illusion
    line(rTopX, rTopY, rTopX + offsetX, rTopY + offsetY);
    line(rBottomX, rBottomY, rBottomX + offsetX, rBottomY + offsetY);
    line(rTopX + offsetX, rTopY + offsetY, rBottomX + offsetX, rBottomY + offsetY);

    // Connect back face to front
    line(left, top, left + offsetX, top + offsetY);
    line(left + offsetX, top + offsetY, right + offsetX, top + offsetY);
    line(right + offsetX, top + offsetY, right + offsetX, bottom + offsetY);
    line(right + offsetX, bottom + offsetY, left + offsetX, bottom + offsetY);
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // 1. Arc (partial circle)
    arc(100, 100, 0, 135, 50); // Center (100, 100), from 0° to 135°, radius 50

    // 2. Bar (rectangle outline)
    rectangle(150, 80, 250, 150); // Rectangle from (150,80) to (250,150)

    // 3. Ellipse (oval outline)
    ellipse(350, 120, 0, 360, 80, 40); // Full ellipse

    // 4. 3D Bar (manual lines)
    draw3DBar(100, 200, 200, 250, 30);

    getch();
    closegraph();
    return 0;
}
