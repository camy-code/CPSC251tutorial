def myfunc(prefix, k, A):
  if k==0:
    print(prefix)
  elif k > 0 and len(A)==0:
    return
  else:
    myfunc( (prefix+ " " + A[0]), k-1, A[1:])
    myfunc(prefix,k, A[1:])
  return

myfunc("", 3, ["1","2","3","4"])

# compute the k size of sets with size(A) objects!
