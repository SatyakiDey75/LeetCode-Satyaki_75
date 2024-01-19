"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val=int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        if head in self.map:
            return self.map[head]
        head1=Node(head.val)
        self.map[head]=head1
        head1.next=self.copyRandomList(head.next)
        head1.random=self.copyRandomList(head.random)
        return head1
    map={}


        # if head is None:
        #     return None
        # val,rand=[],[]
        # p,q=head,head
        # while p:
        #     val.append(p.val)
        #     rand.append(p.random.val if p.random!=None else None)
        #     p=p.next
        # head1=Node(val[0])
        # temp,a=head1,head1
        # rand1=[]
        # rand1.append(head1)
        # for i in range (1,len(val)):
        #     node2=Node(val[i])
        #     temp.next=node2
        #     temp=node2
        #     rand1.append(temp)
        # temp.next=None
        # for i in range(len(rand)):
        #     if rand[i] is not None:
        #         for j in range (len(rand1)):
        #             if rand1[j].val==rand[i]:
        #                 a.random=rand1[j]
        #                 break
        #     else:
        #         a.random=None
        #     a=a.next
            
        # return head1