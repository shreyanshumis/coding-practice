#include <graphics.h>
#include <conio.h>
#include <cmath>

void drawRotatedRectangle(int x, int y, int w, int h, float angle) {
    cleardevice();
    float rad = angle * (3.14159 / 180); // Convert to radians

    // Rectangle points relative to center
    int cx = x + w / 2, cy = y + h / 2;
    int px[4] = {-w / 2, w / 2, w / 2, -w / 2};
    int py[4] = {-h / 2, -h / 2, h / 2, h / 2};

    // Rotate points
    int rx[4], ry[4];
    for (int i = 0; i < 4; i++) {
        rx[i] = cx + px[i] * cos(rad) - py[i] * sin(rad);
        ry[i] = cy + px[i] * sin(rad) + py[i] * cos(rad);
    }

    // Draw rotated rectangle
    line(rx[0], ry[0], rx[1], ry[1]);
    line(rx[1], ry[1], rx[2], ry[2]);
    line(rx[2], ry[2], rx[3], ry[3]);
    line(rx[3], ry[3], rx[0], ry[0]);
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    float angle = 0;

    while (true) {
        drawRotatedRectangle(200, 200, 100, 50, angle);
        int key = getch();

        if (key == 77) { // RIGHT Arrow Key (Clockwise)
            angle += 10;
        } 
        else if (key == 75) { // LEFT Arrow Key (Anti-Clockwise)
            angle -= 10;
        } 
        else if (key == 27) { // ESC Key to Exit
            break;
        }
    }

    closegraph();
    return 0;
}
