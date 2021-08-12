import java.util.HashMap;

public class LRUCache {
    HashMap<Integer, Node> map;
    DoubleLinkedList cache;

    int cap;

    public LRUCache(int capacity) {
        map = new HashMap<>();
        cache = new DoubleLinkedList();
        cap = capacity;
    }

    public void put(int key, int val) {
        Node newNode = new Node(key,val);

        if(map.containsKey(key)) {
            cache.delete(map.get(key));
            cache.addFrist(newNode);
            map.put(key, newNode);
        } else {
            if(map.size() == cap) {
                int last = cache.deleteLast();
                map.remove(key);
            }
            cache.addFrist(newNode);
            map.put(key,newNode);
        }
    }

    public int get(int key) {
        if(!map.containsKey(key)) return -1;
        int val = map.get(key).val;

        this.put(key, val);
        return val;
    }
}


class DoubleLinkedList {
    public Node head;
    public Node tail;

    public DoubleLinkedList() {
        head = new Node(0, 0);
        tail = new Node(0, 0);

        head.next = tail;
        tail.prev = head;
    }

    public void addFrist(Node node) {
        node.prev = head;
        node.next = head.next;

        head.next.prev = node;
        head.next = node;
    }

    public int delete(Node n) {
        int key = n.key;
        n.next.prev = n.prev;
        n.prev.next = n.next;

        return key;
    }

    public int deleteLast() {
        if (head.next == tail) return -1;

        return delete(tail.prev);
    }
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