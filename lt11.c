// # 回文链表

// # 给定一个链表的 头节点 head ，请判断其是否为回文链表。

// # 如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。

思路一：将值复制到数组中后用双指针法（最直观，空间换时间）单向链表的缺点是只能从前往后遍历，不能从后往前看。
但数组可以做到随机访问。所以最简单的想法就是把它变成数组问题。具体步骤：遍历一遍链表，统计节点的总个数，然后用 malloc 动态分配一个对应大小的整型数组（或者直接根据题目提示的最大长度 $10 ^ 5$ 开辟一个大数组）。
再次遍历链表，把每个节点的值依次存入数组中。在数组中使用双指针：左指针指向数组开头（索引 $0$），右指针指向数组结尾。
左右指针同时向中间移动，每次比较两个指针对应的值。如果发现不同，就说明不是回文，返回 false；如果一直相等到两个指针相遇，就是回文，返回 true。
时间复杂度： $O(N)$空间复杂度： $O(N)$（因为借助了额外的数组）

/**
* Definition for singly-linked list.* struct ListNode {
    * int val
    * struct ListNode * next
    *}
*/


bool isPalindrome(struct ListNode * head){
    if (head == NULL){
        return true;
    }
    int count = 0
    struct ListNode *q = head
    while (q != NULL){
        count++;
        q = q -> next;

    }
    int *arr = (int *)malloc(count * sizeof(int));
    q = head;
    for (int i=0;
         i < count;
         i++){
        arr[i] = q -> val
        q = q -> next
    }
    int left = 0;
    int right = count - 1;
    bool isPalind = true;
    while (left < right){
        if (arr[left] != arr[right]){
            isPalind = false;
            break;
        }
        left + +;
        right - -;
    }
    free(arr);
    return isPalind;

}



思路二：快慢双指针+反转后半段链表

这套打法的核心精髓在于：无论链表节点数是奇数还是偶数，它都能完美兼容，并且能让链表无损恢复。

第一步：快慢指针找“前半段的尾巴”
我们要让链表从中间一分为二。怎么找中点？用赛跑法：快指针 fast 每次跑两步，慢指针 slow 每次跑一步。

核心规则： 快指针在往前跳之前，必须确保前面还有两块砖（fast->next != NULL 且 fast->next->next != NULL），否则就立刻停下。

如果是偶数节点（例如 1 -> 2 -> 2 -> 1）：

起跑：slow 和 fast 都在第一个 1。

第一回合：slow 走到第一个 2，fast 走到第二个 2。

判断：fast 发现前面只有一块砖了（下一个是 1，再下一个是空），停下！

结果：slow 停在第一个 2。（完美停在前半段的尾巴）

如果是奇数节点（例如 1 -> 2 -> 3 -> 2 -> 1）：

起跑：slow 和 fast 都在第一个 1。

第一回合：slow 走到 2，fast 走到 3。

第二回合：slow 走到 3，fast 走到最后的 1。

判断：fast 发现前面没砖了（下一个就是空），停下！

结果：slow 停在 3。（完美停在正中间的节点，也就是前半段的尾巴）

第二步：拆卸并反转后半段
找到 slow 之后，slow->next 就是后半段的起始点。

我们把 slow->next 扔进一个“反转机器”（就是我们前面说过的反转辅助函数）。

偶数情况： 原后半段是 2 -> 1 -> NULL，反转后变成 1 -> 2 -> NULL。

奇数情况： 原后半段是 2 -> 1 -> NULL，反转后变成 1 -> 2 -> NULL。

关键点： 反转完成后，我们要记住这个反转链表的新头部，暂且叫它 secondHalf。
此时的链表变成了两条平行的线：

前半段： head 开头（偶数是 1 -> 2，奇数是 1 -> 2 -> 3）

后半段： secondHalf 开头（都是 1 -> 2）

第三步：两端齐头并进大比对
现在我们有两个指针：

p1 站在前半段的开头 head。

p2 站在后半段的开头 secondHalf。

它们同时往后走，每次走一步，对比脚下的值。
结束条件：只要 p2 走完（变成 NULL）就结束。

为什么只看 p2？ 因为在奇数节点（1 -> 2 -> 3 -> 2 -> 1）的情况下，前半段多了一个中间节点 3。反转后的后半段只有 1 -> 2 两个节点。我们只需要比对两头是否对称，中间那个孤独的 3 根本不需要参与比对！所以只要短的后半段（p2）比对完没发现差异，它就是回文。
第四步：打扫战场，恢复原样
比对完之后，我们得出了 true 或 false 的结论。但在交卷之前，我们要把链表接回去。

怎么接？
刚才我们把 slow->next 扔进机器反转成了 secondHalf。
现在，我们只需把 secondHalf 再扔进机器反转一次，它就变回原来的样子了。
然后，让 slow->next 重新牵住变回原样的那段链表。



//最佳标答：
struct ListNode* list_reverse(struct ListNode *p);


bool isPalindrome(struct ListNode* head){
    if(head == NULL || head->next == NULL){
        return true;
    }
    struct ListNode *slow = head;
    struct ListNode *fast = head;
    while(fast->next != NULL && fast->next->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    struct ListNode *prev = list_reverse(slow->next);
    bool isPalind = true;
    struct ListNode *q = head;
    while(prev != NULL){
        if(prev->val != q->val){
            isPalind = false;
            break;
        }
        prev = prev->next;
        q = q->next;
    }
    slow->next = list_reverse(prev);
    return isPalind;
    

}

struct ListNode* list_reverse(struct ListNode *head){//链表反转的最好方法：三指针迭代法！！
    struct ListNode *prev = NULL;
    struct ListNode *curr = head;
    while(curr != NULL){
        struct ListNode *nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}