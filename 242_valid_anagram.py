




'''


Apprach 1 : Sort the strings individually and compare them 


Time - O(nlogn), n being the length of longest string


Approach 2 : Using an extra array

1. Compare the length of both the strins if they are not equal then straight away return from the array
2. Iterate on the string and increremnt in the array at the position corresponding to the value in the first array and decrement in the array accoring to the value in the 2nd array
3. If the array is of all zeros then the stings are valid anagrams, else not


'''
