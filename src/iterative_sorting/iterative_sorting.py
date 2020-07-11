def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        swap(arr, smallest_index, cur_index)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(len(arr) - 1):
        isSorted = True
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                isSorted = False
        if isSorted:
            return arr
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?

We need to dedicate extra space for the counting array, the size of this array
depend on the number of input in the original array. So the space complexity is O(k) space.

For the space we need to iterate to populate the counts array that is O(n), then 
we need to iterate trough counts array that is O(k). The time complexity is O(n+k),
that can be simplify by O(n), that it is linear algorithm.

'''


def counting_sort(arr, maximum=None):
    # Your code here
    # empty array, nothing to sort, return arr
    if not arr:
        return arr
    # Getting maximum value from array if not given in parameter
    if not maximum:
        m = max(arr) + 1
    else:
        m = maximum + 1
    # Initialized counts array
    counts = [0] * m
    # set populate counts array
    for i in arr:
        counts[i] += 1
    # sorting
    k = 0
    for i in range(m):
        for j in range(counts[i]):
            if (arr[k] < 0):
                return "Error, negative numbers not allowed in Count Sort"
            arr[k] = i
            k += 1
    return arr
