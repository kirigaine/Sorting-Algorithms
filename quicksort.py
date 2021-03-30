"""
Algorithm: QUICK SORT
Best: O(nlogn)
Average: O(nlogn)
Worst: O(n^2)
Space: 0(logn)
Pros:
    + Low overhead
    + Efficient
Cons:
    - Moderately complex logically
    - Worst case time complexity happens with sorted data
    - Random pivots can result in occasional longer time complexity
    - Unstable
"""
from random import randint

def main():

    # Create 3 data sets and test sorting algorithm
    A = [4,3,2,4,6,2]
    print("A Unsorted: ",end='')
    myprint(A)
    randomizedQuickSort(A,0,(len(A)-1))
    print("A Sorted: ",end='')
    myprint(A)

    B = [3,1,2]
    print("B Unsorted: ",end='')
    myprint(B)
    randomizedQuickSort(B,0,(len(B)-1))
    print("B Sorted: ",end='')
    myprint(B)

    C = [-1,-3]
    print("C Unsorted: ",end='')
    myprint(C)
    randomizedQuickSort(C,0,(len(C)-1))
    print("C Sorted: ",end='')
    myprint(C)

def partition(A, p, r):
    # Select pivot
    x = A[r]
    i = p-1
    for j in range(p,r,1):
        # Compare element to pivot value
        if A[j] <= x:
            i += 1
            # Swap A[i] with A[j] if value less than or equal to pivot
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    # Swap A[i+1] with A[r]
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return (i+1)

def randomizedPartition(A, p, r):
    # Generates a random pivot between the lower and upper index, swamps the pivot with the last value
    i = randint(p+1,r)
    temp = A[r]
    A[r] = A[i]
    A[i] = temp
    return partition(A,p,r)

def randomizedQuickSort(A, p, r):
    # p < r used to terminate recursive call
    if p < r:
        q = randomizedPartition(A,p,r)
        # Sort using partition
        randomizedQuickSort(A,p,(q-1))
        randomizedQuickSort(A,(q+1),r)

def myprint(array):
    for each in array:
        print(str(each),end=' ')
    print("")

main()