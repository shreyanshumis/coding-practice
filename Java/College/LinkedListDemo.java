import java.util.LinkedList;

public class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList<String> linkedList = new LinkedList<>();
        linkedList.add("Java");
        linkedList.add("Python");
        linkedList.add("C++");
        linkedList.add("JavaScript");

        System.out.println("Original LinkedList: " + linkedList);

        linkedList.addFirst("C#");
        System.out.println("LinkedList after adding at the beginning: " + linkedList);

        linkedList.addLast("Ruby");
        System.out.println("LinkedList after adding at the end: " + linkedList);

        linkedList.removeFirst();
        System.out.println("LinkedList after removing the first element: " + linkedList);

        linkedList.removeLast();
        System.out.println("LinkedList after removing the last element: " + linkedList);

        boolean containsJava = linkedList.contains("Java");
        System.out.println("Does it have java or not?" + containsJava);

        int size = linkedList.size();
        System.out.println("Size of the LinkedList: " + size);

        System.out.println("Elements of the LinkedList:");
        for (String element : linkedList) {
            System.out.println(element);
        }

        linkedList.clear();
        System.out.println("LinkedList after clearing: " + linkedList);
    }
}
