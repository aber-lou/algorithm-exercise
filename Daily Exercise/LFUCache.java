public class LFUCache {

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