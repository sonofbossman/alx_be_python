# num_range = range(1, 10)
# counter = 0
# for num in num_range:
#   if num%2==0:
#     counter += 1
#     print(num)
# print(f"We have {counter} even numbers")

# for num in range(1, 101):
#   if num%3!=0 and num%5!=0:
#     print(num)

# for _ in range(4):
#   for _ in range(5):
#     print("#", end="")
#   print()

for i in range(1, 11):
  # Outer loop iterates through rows (multiplication factors)
  for j in range(1, 11):
    # Inner loop iterates through columns (other factors)
    product = i * j
    print(f"{i} x {j} = {product}", end="\n")  # Print with tabs for better formatting
  print()  # Move to a new line after each row