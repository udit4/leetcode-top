



'''


Approach 1 :: Naive


1. Make all the substrinngs from the given string
2. For each substring check, check whether it is valid or not (by counting the number of unique-elements)
3. If is satifiies the condition then store this

Complexity - O(n^3)



Approach 2 :: Linear (Sliding Window)


1. Make two poiters (start and end)
2. Move end to right till the give condition is not met, if the substring is valid store this and move end to right
3. If the sub-string exceed the k then move the start pointer to right
4. Return the substring wiht maximum length satisfying the condition.

'''

