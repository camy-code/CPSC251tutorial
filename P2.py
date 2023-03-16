def rec_grayCode(n):
  if n == 1:
    return ["0", "1"]
  else:
    sub_cases = rec_grayCode(n-1)
    result = []

    for s in sub_cases:
      result.append("0" + s)

    for s in sub_cases[::-1]: # Reverse of the subcases
      result.append("1" + s)
    
  return result


print(rec_grayCode(3))
