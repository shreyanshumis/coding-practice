public class CuboidVolume {
    public static void main(String[] args) {
        double length = 3.5;
        double breadth = 2.0;
        double height = 4.8;

        double volume = calculateCuboidVolume(length, breadth, height);

        System.out.println("Cuboid Volume: " + volume);
    }

    static double calculateCuboidVolume(double length, double breadth, double height) {
        return length * breadth * height;
    }
}
