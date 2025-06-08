def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            print()
            item = input("Enter item name: ")
            if item not in shopping_list:
                shopping_list.append(item)
                print(f"✅ {item} has been added to the shopping list!")
            else:
                print(f"❌ {item} has been added to the shopping list already!")
        elif choice == '2':
            # Prompt for and remove an item
            print()
            item = input("Enter the name of item to remove: ")
            if item not in shopping_list:
                print(f"❌ {item} was not found on the list!")
            else:
                shopping_list.remove(item)
                print(f"✅ {item} has been removed successfully.")
        elif choice == '3':
           # Display the shopping list
           print()
           if shopping_list:
               for i, item in enumerate(shopping_list, start=1):
                   print(f"{i}. {item}")
           else:
               print("Your shopping list is empty!")
        elif choice == '4':
            print()
            print("Goodbye!")
            break
        else:
            print()
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()