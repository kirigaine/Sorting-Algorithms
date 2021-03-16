"""
Algorithm: BUBBLE SORT
Best: O(n)
Average: O(n^2)
Worst: O(n^2)
Space: 0(1)
Pros:
    +
Cons:
    -
"""

def main():
    A = [4,3,2,4,6,2]
    print("A Unsorted: ",end='')
    myprint(A)
    bubbleSort(A)
    print("A Sorted: ",end='')
    myprint(A)

    B = [3,1,2]
    print("B Unsorted: ",end='')
    myprint(B)
    bubbleSort(B)
    print("B Sorted: ",end='')
    myprint(B)

    C = [-1,-3]
    print("C Unsorted: ",end='')
    myprint(C)
    bubbleSort(C)
    print("C Sorted: ",end='')
    myprint(C)

    D = [1,2,3,4,5,6]
    print("D Unsorted: ",end='')
    myprint(D)
    bubbleSort(D)
    print("D Sorted: ",end='')
    myprint(D)

def bubbleSort(A):
    
    # Determine size of the array
    size = len(A)

    # Use iterating for-loop of array size to determine number of indexes "swapped" / placed correctly
    for i in range(size):
        # Create a boolean to cancel loop if array is already sorted
        has_swapped = False
        for j in range(0, size-i-1):
            if A[j] > A[j+1]:
                # If index to left of right index, swap them and flag boolean
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                has_swapped = True

        # If nothing swapped, array must be sorted. Break loop
        if not has_swapped:
            break


def myprint(array):
    for each in array:
        print(str(each),end=' ')
    print("")

main()