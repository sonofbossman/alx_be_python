def perform_operation(num1, num2, operation):
  """A function that performs basic arithmetic operations."""
  match operation:
    case 'add':
      return num1+num2
    case 'subtract':
      return num1 - num2
    case 'multiply':
      return num1 * num2
    case 'divide':
      if num2 != 0:
        return num1 / num2
      elif num2 == 0:
        return "Cannot divide by zero."
    case _:
      return "Invalid operation specified!"