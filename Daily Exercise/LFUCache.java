import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

import org.graalvm.compiler.graph.Node;

class LFUCache {
    int minfreq, capacity;
    Map<Integer, Node> key_table;
    Map<Integer, LinkedList<Node>> freq_table;

    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.minfreq = 0;
        this.key_table = new HashMap<Integer, Node>();
        this.freq_table = new HashMap<Integer, LinkedList<Node>>()
    }

    public int get(int key) {
        // 没有值，直接返回-1
        if(capacity == 0) { 
            return -1;
        }

        // 节点数组中没有值，也直接返回
        if(!key_table.containsKey(key)) {
            return -1;
        }

        
        Node node = key_table.get(key);
        int val = node.val, freq = node.frequency;
        freq_table.get(freq).remove(node);
        if(freq_table.get(freq).size() == 0) {
            freq_table.remove(freq);

            if(minfreq == freq) {
                minfreq += 1;
            }
        }
        LinkedList<Node> list = freq_table.getOrDefault(freq+1, new LinkedList<Node>());
        list.offerFirst(new Node(key,val,freq+1));
        freq_table.put(freq+1, list);
        key_table.put(key, freq_table.get(freq+1).peekFirst());
        return val;
    }

    public void put(int key, int value) {
        if (capacity == 0) {
            return;
        }

        if(!key_table.containsKey(key)) {
            if(key_table.size() == capacity)  {
                Node node = freq_table.get(minfreq).peekFirst();
                key_table.remove(node.key);
                freq_table.remove(minfreq).pollLast();
                if(freq_table.get(minfreq).size() == 0) {
                    freq_table.remove(minfreq);
                }
            }

            LinkedList<Node> list = freq_table.getOrDefault(1, new LinkedList<Node>());
            list.offerFirst(new Node(key,value,1));
            freq_table.put(1, list);
            key_table.put(key, freq_table.get(1).peekFirst());
            minfreq = 1;
        } else {
            Node node = key_table.get(key);
            int freq = node.frequency;
            freq_table.get(freq).remove(node);
            if(freq_table.get(freq).size() == 0) {
                freq_table.remove(freq);
                if(minfreq == freq) {
                    minfreq += 1;
                }
            }
            LinkedList<Node> list = freq_table.getOrDefault(freq+1, new LinkedList<Node>());
            list.offerFirst(new Node(key, value, freq+1));
            freq_table.put(freq+1, list);
            key_table.put(key, freq_table.get(freq+1).peekFirst());
        }
    }

}

// 节点对象，包含Key，Val,当前节点出现的频率
class Node {
    int key;
    int val;
    int frequency;

    public Node(int key,int val,int frequency) {
        this.key = key;
        this.val = val;
        this.frequency = frequency;
    }

}