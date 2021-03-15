"""
Algorithm: HEAP SORT
Best: O(nlogn)
Average: O(nlogn)
Worst: O(nlogn)
Space: 0(1)
Pros:
    + Heapsort is fast
    + Doesn't require extra memory in place
Cons:
    -
"""
import math
def main():

    A = [4,3,2,4,6,2]
    print("A Unsorted: ",end='')
    myprint(A)
    heap_sort(A,len(A))
    print("A Sorted: ",end='')
    myprint(A)

    B = [3,1,2]
    print("B Unsorted: ",end='')
    myprint(B)
    heap_sort(B,len(B))
    print("B Sorted: ",end='')
    myprint(B)

    C = [-1,-3]
    print("C Unsorted: ",end='')
    myprint(C)
    heap_sort(C,len(C))
    print("C Sorted: ",end='')
    myprint(C)

def maxHeapify(A, i, heapsize):
    # Find the left and right child. Default provided input as largest value, will be changed if not
    # Left child's index
    l = (2*i) + 1
    # Right child's index
    r = (2*i) + 2
    largest = i

    # Make sure nodes exist, and if they do, if their value is larger than largest, replace largest
    if l < heapsize and A[l] > A[i]:
        largest = l
    if r < heapsize and A[r] > A[largest]:
        largest = r

    # If largest isn't i, then we must swap values and recall to double-check we maintain a max-heap
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        maxHeapify(A, largest, heapsize)

def buildMaxHeap(A, size):
    # for(i=(floor(size/2)); i>=0; i--)
    for i in range(math.floor(size/2),-1,-1):
        maxHeapify(A,i,size)

def heap_sort(A, size):
    # Build max-heap to enable heapsort to work
    buildMaxHeap(A,size)

    # Extract largest values one at a time and call maxHeapify on (size-1) until place in correct order
    # for(i=(size-1); i>=0; i--)
    for i in range((size-1),-1,-1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        maxHeapify(A,0,i)


def myprint(array):
    for each in array:
        print(str(each),end=' ')
    print("")

main()