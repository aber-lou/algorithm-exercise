import java.util.HashMap;

public class LRUCache {
    HashMap<Integer, Node> map;



}


class DoubleLinkedList {
    public Node head;
    public Node tail;
}


class Node {
    public int key;
    public int val;
    public Node prev;
    public Node next;
    
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}