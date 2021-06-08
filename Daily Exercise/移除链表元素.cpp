struct ListNode
{
    int val;
    ListNode *next;
    ListNode(): val(0), next(nullptr) {}
    ListNode(int x) : val(x),next(nullptr) {}
    ListNode(int x, ListNode *next): val(x), next(next){}

};


class Solution
{
private:
    /* data */
public:
    Solution(/* args */);
    ~Solution();

    ListNode* removeElements(ListNode* head, int val) {
        struct ListNode* dummyHead = new ListNode(0, head);
        struct ListNode* temp = dummyHead;
        while (temp->next != nullptr) {
        {
            if(temp->next->val == val) {
                temp->next = temp->next->next;
            }else {
                temp = temp->next;
            }
        }
        return dummyHead->next;
    }
};

Solution::Solution(/* args */)
{

}

Solution::~Solution()
{

}


