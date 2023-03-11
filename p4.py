def permut(array):
    if len(array) == 1:
        return [array]
    res = []
    for permutation in permut(array[1:]):
        for i in range(len(array)):
            res.append(permutation[:i] + array[0:1] + permutation[i:])
    return res

arr =permut([1,2,3])


# This is just where I print the array!
for i in arr:
  print(i)

# I got this from stackoverflow
# link: https://stackoverflow.com/questions/13109274/python-recursion-permutations
