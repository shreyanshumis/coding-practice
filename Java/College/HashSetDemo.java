import java.util.HashSet;
import java.util.Iterator;

public class HashSetDemo {
    public static void main(String[] args) {
        HashSet<String> hashSet = new HashSet<>();
        hashSet.add("Java");
        hashSet.add("Python");
        hashSet.add("C++");
        hashSet.add("JavaScript");

        System.out.println("Original HashSet: " + hashSet);

        hashSet.add("Java");

        System.out.println("HashSet after adding a duplicate element: " + hashSet);

        hashSet.remove("C++");
        System.out.println("HashSet after removing 'C++': " + hashSet);

        boolean containsJava = hashSet.contains("Java");
        System.out.println("Is 'Java' present in the HashSet? " + containsJava);

        int size = hashSet.size();
        System.out.println("Size of the HashSet: " + size);

        System.out.println("Elements of the HashSet:");
        Iterator<String> iterator = hashSet.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }

        hashSet.clear();
        System.out.println("HashSet after clearing: " + hashSet);
    }
}
