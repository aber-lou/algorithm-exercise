public class LFUCache {

}

class LinkedList {
    Node head;
    Node tail;

    public LinkedList() {
        this.head = new Node(0, 0, 100000);
    }
}

class Node {
    int key;
    int val;
    int frequency;
    Node prev;
    Node next;

    public Node(int key,int val,int frequency) {
        this.key = key;
        this.val = val;
        this.frequency = frequency;
    }

}