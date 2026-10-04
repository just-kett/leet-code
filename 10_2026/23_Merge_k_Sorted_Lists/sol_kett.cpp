#include <vector>

using namespace std;

 struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergetwoList(ListNode* a, ListNode* b) {
        ListNode start(0);
        ListNode* tail = &start;
        while(a != nullptr && b != nullptr) {
            if (a->val <= b->val) {
                tail->next = a;
                a = a->next;
            }
            else {
                tail->next = b;
                b = b->next;
            }
            tail = tail->next;
        }
        if (a != nullptr) {
            tail->next = a;
        }
        else {
            tail->next = b;
        }
        return start.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return nullptr;
        }
        while (lists.size() > 1) {
            vector<ListNode*> merge;
            for (int i = 0; i < lists.size(); i += 2) {
                ListNode* a = lists[i];
                ListNode* b = nullptr;
                if (i + 1 < lists.size()){
                    b = lists[i + 1];
                }
                merge.push_back(mergetwoList(a, b));
            }
            lists = merge;
        }
        return lists[0];
    }
};