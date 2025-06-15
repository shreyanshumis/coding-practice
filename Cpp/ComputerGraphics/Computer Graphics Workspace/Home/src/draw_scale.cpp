#include <graphics.h>
#include <conio.h>

void drawScaledRectangle(float scaleFactor) {
    cleardevice();
    
    int x = 200, y = 200; // Top-left corner
    int width = 100 * scaleFactor, height = 50 * scaleFactor;
    
    rectangle(x, y, x + width, y + height); // Draw scaled rectangle
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    float scaleFactor = 1.0; // Initial scaling factor

    while (true) {
        drawScaledRectangle(scaleFactor);
        
        int key = getch(); // Wait for user input

        if (key == 72) { // UP Arrow Key -> Zoom In
            scaleFactor += 0.1;
        } 
        else if (key == 80) { // DOWN Arrow Key -> Zoom Out
            scaleFactor = max(0.1f, scaleFactor - 0.1f); // Prevents negative scaling
        } 
        else if (key == 27) { // ESC Key -> Exit
            break;
        }
    }

    closegraph();
    return 0;
}

