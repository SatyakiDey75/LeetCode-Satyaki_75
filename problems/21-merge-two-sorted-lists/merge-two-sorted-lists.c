/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int count(struct ListNode *start){
   struct ListNode *q;
   q = start;
   int c=0;
   while (q != NULL) {
      c++;
      q=q->next;
   }
   return c;
}

void add_any(struct ListNode *start,int m) {
    struct ListNode *q,*temp;
    temp = malloc(sizeof(struct ListNode));
    temp->val=m;
    q=start;
    while (q->next !=NULL && q->next->val < m)
        q=q->next;
    temp -> next = q->next;
    q->next=temp;
}

struct ListNode* meow(struct ListNode* girl, struct ListNode* boy) {
    struct ListNode *q;
    q=girl;
    while (q!=NULL) {
        add_any(boy,q->val);
        q=q->next;
    }
    return boy;
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if (list1==NULL)
        return list2;
    else if (list2==NULL)
        return list1;
    else {    
        int c1=count(list1),c2=count(list2);
        if (c1==1 && c2==1){
            if (list1->val<list2->val){
                add_any(list1,list2->val);
                return list1;}
            else{
                add_any(list2,list1->val);
                return list2;}
        }
        else if (c1==1){
            add_any(list2,list1->val);
            return list2;
        }
        else if (list1->val>list2->val)
            return meow(list1,list2);
        else
            return meow(list2,list1);
    }
}