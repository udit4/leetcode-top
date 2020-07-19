

'''


Approach 1 : Naive 

1.) Compute all the substrings of the given string 
2.) For each substring compute the occurece of each character and check if the min-occurence of each character is >= k
3.) Complexity : O(n^3)



Approach 2 : Recursion

if len(s) < k return 0 (because the length of string is less than k)

1.) Check the frequency of least occuring character in s, let it be n
    if(n) >= k: return n  (because the least frequency is more than k)
2.) Split the string on this char (as this char can never be the part of the solution)
3.) for each substring of the spliited string, run this funciton recursively 
4.) Complexity  O(nlogn)

'''




    