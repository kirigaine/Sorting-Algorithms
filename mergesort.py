"""
Algorithm: MERGE SORT
Best: O(nlogn)
Average: O(nlogn)
Worst: O(nlogn)
Space: 0(n)
Pros: Faster than insertion sort
Cons: Requires more in place memory
"""
import math
def main():

    A = [1,3,6,4,1,2]
    print("A Unsorted: ",end='')
    myprint(A)
    merge_sort(A,0,(len(A)-1))
    print("A Sorted: ",end='')
    myprint(A)

    B = [3,2,1]
    print("B Unsorted: ",end='')
    myprint(B)
    merge_sort(B,0,(len(B)-1))
    print("B Sorted: ",end='')
    myprint(B)

    C = [-1,-3]
    print("C Unsorted: ",end='')
    myprint(C)
    merge_sort(C,0,(len(C)-1))
    print("C Sorted: ",end='')
    myprint(C)

# p is beginning index of array (which is 0), r is end index (which is length of array - 1)
def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A,q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = []
    right = []
    
    # for(i = 0; i < n1; i++)
    for i in range(0,n1,1):
        left.append(A[p+i])
    left.append(1000001)
    # 1000001 is an arbitrary value based on what the max value your ints will be, is supposed to be INFINITY

    # for(j = 0; j < n2; j++)
    for j in range(0,n2,1):
        right.append(A[q+j+1])
    right.append(1000001)
    # 1000001 is an arbitrary value based on what the max value your ints will be, is supposed to be INFINITY


    i = j = 0
    k = p
    while (k <= r):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

def myprint(array):
    for each in array:
        print(str(each),end=' ')
    print("")

main()