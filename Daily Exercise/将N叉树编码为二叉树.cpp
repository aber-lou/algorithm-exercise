class Node {
    public:
        int val;
        vector<Node*> children;

        Node(){}

        Node(int _val) {
            val = _val;
        }

        Node(int _val, vector<Node*> _children) {
            val = _val;
            children = _children;
        }
};


struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr){}
};

class Codec {
    public:
    
    TreeNode* encode(Node* root) {
        if(!root) {
            return nullptr;
        }

        TreeNode *newRoot = new TreeNode(root->val);
        TreeNode *cur = nullptr;

        if (!root->children.empty())
        {
            newRoot->left = encode(root->children[0]);
            cur = newRoot->left;
        } 

        for (size_t i = 1; i < root->children.size(); i++)
        {
            cur->right = encode(root->children[i]);
            cur = cur->right;
        }

        return newRoot;
    }

    Node* decode(TreeNode* root) {
        if (!root)
        {
            return nullptr;
        }

        Node *newRoot = new Node(root->val);

        TreeNode *cur = nullptr;
        if (root->left) 
        {
            newRoot->children.push_back(decode(root->left));
            cur = root->left;
        } 
        while (cur && cur->right)
        {
            newRoot->children.push_back(decode(cur->right));
            cur = root->right;
        }

        return newRoot;
    }
};
