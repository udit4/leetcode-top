


'''

Approach :: Naive 

1. Run 2 loops and check for each character if it occurs again in the string
2. Break on the fist characeter which satisfies this condition 



Approach 2 :: Two pass on string

1. Iterate on string once and store the element-frequeny in a hash-map.
2. Iterate on string again and check for each character their value in the hash-map, break on the first character found.


Approach 3 :: One pass on string

1. Iterate on string and make an elemnent-frequency map.
2. Store the values in the map (first_occurence_index, count)
3. Iterate on the map, check for count == 1 and min(first_occurence_index)

'''

