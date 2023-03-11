# NOT MY CODE I GOT IT FROM GEEKS FOR GEEKS
# THE LINK is here!

# https://www.geeksforgeeks.org/generate-n-bit-gray-codes/

# I comment annotations.

import math as mt
 
# This function generates all n bit Gray
# codes and prints the generated codes
def generateGrayarr(n):
 
    # base case
    if (n <= 0):
        return
 
    # 'arr' will store all generated codes
    arr = list()
 
    # start with one-bit pattern
    arr.append("0")
    arr.append("1")
 
    # Every iteration of this loop generates
    # 2*i codes from previously generated i codes.
    i = 2       # This is the variable for 2 to the power of 
    j = 0       # This is just the loop variable
    while(True):
 
        if i >= (1 << n): # I have a explanation for << at the bottom
            break   # we leave the loop
     
        # Enter the previously generated codes
        # again in arr[] in reverse order.
        # Nor arr[] has double number of codes.
        for j in range(i - 1, -1, -1):
            arr.append(arr[j])
            print(arr)
            # The above code grabs the letthand bits that we need to copy over
 
        # append 0 to the first half
        for j in range(i):
            arr[j] = "0" + arr[j]
 
        # append 1 to the second half
        for j in range(i, 2 * i):
            arr[j] = "1" + arr[j]

        i = (i << 1) # This is effectively multiplying by 2. 
        # The << is a logical shift left so if we have the bit string 1111.
        #  When we LSL that string we get 1110.
        # Append a zero at the right hand side, slide everything left
        # and discard the leftmost bit.


 
    # print contents of arr[]
    for i in range(len(arr)):
        print(arr[i])
 
# Driver Code
generateGrayarr(2)
