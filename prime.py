def prime_decomposition(n):
  factors = []
  divisor = 2
  while n > 1:
      while n % divisor == 0:
          factors.append(divisor)
          n //= divisor
      divisor += 1
  return factors

for i in range(1, 101):
  print(f"Prime decomposition of {i}: {prime_decomposition(i)}")
