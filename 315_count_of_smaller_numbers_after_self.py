


'''

Approach 1 ::Brute Force 

1. Using two loops and for each element counting the number of elements smaller that it
2. Updating the count in the separate array


Time - O(n^2)
Space - O(n)


Approach 2 :: Self Balancing Trees

1. Using self-balancing trees like AVL, Redi-Black we can use the idea that in this at the node
2. All smaller elements would be in the left subtree and all larger elements would be in the right subtree
3. So while inserting a new key all the elements smaller than that would be in the left subtree, so we can store this count/information for the key

Complexity - O(nlogn)
Space - O(n)


'''

