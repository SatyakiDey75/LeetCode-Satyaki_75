def merge(arr,l,m,r):
    n1,n2=m-l+1,r-m
    L,R=[0]*(n1),[0]*(n2)
    for i in range(0,n1):
        L[i]=arr[l+i]
    for j in range(0,n2):
        R[j]=arr[m+1+j]
    i,j,k=0,0,l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1

def mergeSort(arr,l,r):
    if l<r:
        m=l+(r-l)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)

class Solution(object):
    def sortArray(self, nums):
        # mergeSort(nums,0,len(nums)-1)
        nums.sort()
        return nums