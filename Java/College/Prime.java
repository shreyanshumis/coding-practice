public class Prime {
    public static void main(String[] args) {
        int number = 29; // Change this to the number you want to check

        if (isPrime(number)) {
            System.out.println(number + " is a prime number.");
        } else {
            System.out.println(number + " is not a prime number.");
        }
    }

    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false; // Numbers less than or equal to 1 are not prime
        }

        // Check from 2 to the square root of the number
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false; // If divisible by any number in this range, it's not prime
            }
        }

        return true; // If not divisible by any number in the range, it's prime
    }
}
