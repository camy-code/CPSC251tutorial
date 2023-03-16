def permut(array):
    if len(array) == 1: # Can also go with len(array) == 0 and returning empty array
        return [array]
    res = []
    for permutation in permut(array[1:]):
        for i in range(len(array)):
            res.append(permutation[:i] + array[0:1] + permutation[i:])
    return res

print(permut([1,2,3]))


# I got this from stackoverflow
# link: https://stackoverflow.com/questions/13109274/python-recursion-permutations
