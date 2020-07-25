




'''


Approach : Using recursion to print all the subsequences of an array

1. Each element of array/string have 2 options, either to be a part of substring or not be a part of it.
2. Using this info, we can use recursion to each position once to include the element and other part to exlucde it.

'''





class Solution:
    def __init__(self, arr):
        self.arr = arr
        self.allSubsequence(0, [])
        return 

   
    # this function computes the subsequence for the input-array       
    def allSubsequence(self, currentIndex, subSequence):

        if currentIndex == len(self.arr):
            if len(subSequence) != 0:
                print(subSequence)
        else:
            # recursice call 
            self.allSubsequence(currentIndex+1, subSequence)
            self.allSubsequence(currentIndex+1, subSequence + [self.arr[currentIndex]])
    
        return
        



s = Solution([1, 2, 3])


