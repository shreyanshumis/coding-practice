public class StringMethods {
    public static void main(String[] args) {
        String name  = "Shrey"; //0-4 Index
        System.out.println("String = "+ name);
        System.out.println("==========");
        int value = name.length();

        System.out.println("Length:" + value);//returns length

        System.out.println("Lower case:" + name.toLowerCase());//converts to lower case

        System.out.println("Upper case:" + name.toUpperCase());//converts to upper case

        String trimName = "    Shrey   ";
        System.out.println("Untrimmed :" + trimName);
        System.out.println("Trimmed string:" + trimName.trim()); //removes trailing and leading spaces(L and R)

        System.out.println("Substring from Index 2 & ending with 5:" + name.substring(2,5)); //gives a substring(beginning index/end index inside brackets)

        System.out.println("Replaced y with x:" + name.replace('y', 'x')); //replaces characters

        System.out.println("Replaced Sh with Manta:" + name.replace("Sh", "Manta"));//replaces string

        System.out.println("Starts with Sh?:" + name.startsWith("Sh"));//if it starts with this string or not

        System.out.println("Ends with ey?:" + name.endsWith("ey"));//if it ends with this string or not

        System.out.println("Character at 0:" + name.charAt(0)); //returns a character at an index

        System.out.println("Index of 'h' :" + name.indexOf('h'));//returns the first index of the given char/string
        System.out.println("Index of 'h' but from an index of 3:" + name.indexOf('h',3));//same but starting point is not 0th index

        System.out.println("Last Index of:" + name.lastIndexOf('y'));//Returns a last Index of a char/string
        System.out.println("Last Index of:" + name.lastIndexOf('y', 4)); //same but from a given index instead of 0

        System.out.println("Equals:" + name.equals("Shrey")); //checks if name is equal to the given string(Case sensitive)
        System.out.println("Equals ignore case:" + name.equalsIgnoreCase("sHrEy"));//ignores the case

//      escape sequence characters : \n , \t, \'', \"", \\ etc.
    }
}
