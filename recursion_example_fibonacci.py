def fibonacci(n):
  #bazični slučaj
  if n==0 or n == 1:
    return n
  #rekurzivni slučaj
  a = fibonacci(n-1)
  b = fibonacci(n-2)
  return a + b

fibonacci(6)