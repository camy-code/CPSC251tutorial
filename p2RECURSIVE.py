def rec_grayCode(n):
  if n ==1:
    return ["0","1"]
  else:
    arr1 = rec_grayCode(n-1)
    arr2 = rec_grayCode(n-1)
    arr2.reverse()

    for i in range(len(arr1)):
      arr1[i] = "0" + arr1[i]

    for i in range(len(arr2)):
      arr2[i] = "1" + arr2[i]
    
  return arr1 + arr2



print(rec_grayCode(3))
array =(rec_grayCode(3))
for i in array:
  print(i) 
