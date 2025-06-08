from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now()
  return current_date

def calculate_future_date(current_date, num_of_days):
  future_date = current_date + timedelta(days=num_of_days)
  return future_date

def main():
  try:
    current_date = display_current_datetime()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")
    num_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(current_date, num_of_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
  except Exception as e:
    print(e)

if __name__ == "__main__":
  main()