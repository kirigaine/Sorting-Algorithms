"""
Algorithm: INSERTION SORT
Best: O(n)
Average: O(n^2)
Worst: O(n^2)
Space: 0(1)
Why Use: Can be a bit slower, but doesn't require extra memory. Simple.
"""
def main():
    print("A Unsorted: ",end='')
    A = [5,2,4,6,1,3]
    myprint(A)
    insertion_sort(A)
    print("A Sorted: ",end='')
    myprint(A)

    B = [3,2,1]
    print("B Unsorted: ",end='')
    myprint(B)
    insertion_sort(B)
    print("B Sorted: ",end='')
    myprint(B)

    C = [-1,-3]
    print("C Unsorted: ",end='')
    myprint(C)
    insertion_sort(C)
    print("C Sorted: ",end='')
    myprint(C)

def insertion_sort(A):
    # for(j=1; j<A.length; j++)
    for j in range(1, len(A), 1):
        key = A[j]
        #print("Key: " + str(key) + " ", end='')  key = 2, j = 1, i = 0
        #print("j: " + str(j) + " ", end='')
        i = j - 1
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        #print("i: " + str(i))
        A[i+1] = key

def myprint(array):
    for each in array:
        print(str(each),end=' ')
    print("")

main()