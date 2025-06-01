size = int(input("Enter the size of the pattern: "))
pattern_size = size
while size >= 1:
  for _ in range(pattern_size):
    print("*", end="")
  print()
  size -= 1
