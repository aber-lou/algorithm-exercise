import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

import javax.management.QueryEval;

import org.w3c.dom.Node;

public class Tree_Width {


    public static void w(Node head) {
        if (head == null) return ;

        Queue<Node> queue = new LinkedList<>();
        queue.add(head);
        while(!queue.isEmpty()) {
            Node cur = queue.poll();
            System.out.println(cur);
            if (cur.left != null) {
                queue.add(cur.left);
            }
            if (cur.right != null) {
                queue.add(cur.right);
            }
        }

    }

    public static int treeWidth(Node node) {
        if (head == null) { return 0; }

        Queue<Node> queue = new LinkedList<>();
        queue.add(head);

        HashMap<Node, Integer> levelMap = new HashMap<>();

        levelMap.put(head, 1);
        int curLevel = 1;
        int curLevelNodes = 0;
        int max = Integer.MIN_VALUE;
        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            int curNodeLevel = levelMap.get(cur);
            if (curNodeLevel == curLevel) {
                curLevelNodes++;
            } else {
                max = Math.max(max, curLevelNodes);
                curLevel++;
                curLevelNodes = 1;
            }

            if (cur.left != null) {
                levelMap.put(cur.left, curNodeLevel+1);
                queue.add(cur.left);
            }
            if (cur.right != null) {
                levelMap.put(cur.right, curNodeLevel+1);
                queue.add(cur.right);
            }
            
        }

    }
}
