




'''


Approach 1 : With extra space 


1. Use an extra array with length = n and having all the variables as 0.
2. Iterate on the input array now and using a variable count, replace the value in the second array with the non-zero elements.
3. The second array would now be having the elements in order.


Time - O(n)
Space - O(n)


Approach 2 : Without extra space

1. Make a variable count = 0
2. Iterate on the array and for any ith non-zero element do arr[count] = arr[i] and count +=1 
3. Now when i reaches to end do : while (count<n): arr[count++] = 0 (make all the elements zero)

Time - O(n)
Space - O(1)

'''




