import java.util.Stack;

public class TreeOrderUnRecur {
    
    public static void inOrderUnRecur(Node head) {
        System.out.print("in - order:");

        if(head != null) {
            Stack<Node> stack = new Stack<>();

            while( !stack.isEmpty() || head != null ) {
                if (head != null) {
                    stack.push(head);
                    head = head.left;
                } else {
                    head = stack.pop();
                    System.out.print(head.val + "");
                    head = head.right;
                }
            }
        }

        System.out.println();
    }
}
