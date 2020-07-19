



'''

Approach 1 ::


1. Make an element-frequency map for array.
2. Iterate on this map and make a priority-queue with priortity give on the basis of count (count, element_value)
3. Pop the top-k element from this queue.

Complexity - O(n) + klog(d) [d = size of element-frequncy map]

Approach 2 ::

1. Using the idea that max(frequency) of any element can be n, which is the size of array.
2. Initialise an empty array of size (n) with all values -1 (topKArray)
3. Make element-frequecy map of the array
4. Iterate on this element0-frequency map and set the value in the topKArray[index i.e. count_of_element] = value i.e element
5. Iterate on the topKArray starting from (N-1)th index and retrun the first k values which are not -1.


Complexity - O(n) + O(n) ~ 2O(n)
'''
