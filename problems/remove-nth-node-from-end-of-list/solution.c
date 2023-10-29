
int count(struct ListNode* start){
   struct ListNode *q;
   q = start;
   int c=0;
   while (q!= NULL) {
      c++;
      q=q->next;
   }
   return c;
}

void delpos(struct ListNode* start, int pos) {
   struct ListNode *q, *temp;
   q=start;
   for (int c=0; c<pos-2; c++)
      q=q-> next;
   temp=q->next;
   if (temp->next==NULL)
      q->next=NULL;
   else
      q->next=temp->next;
   free(temp);
}


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
   int c=count(head);
   int s=c-n+1;
   if (c==1){
      return NULL;
   }
   else if (c==n)
      head=head->next;
   else
      delpos(head,s);
   return head;
}