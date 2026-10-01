
def main():
    print("Expense Tracker")
    print("--------------------------------------------------")


    expenses = {"Groceries": 0.0,"Personal": 0.0,"Investment": 0.0,"Bills": 0.0,"Entertainment": 0.0
    }
    try:
        while True:
            print("\nOptions:")
            print("1. Set Expense")
            print("2. Show All Expenses & Total")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
            
                category = input("Enter category name: ").title()
                if category in expenses:
                    amount = float(input("Enter amount: "))
                    expenses[category] = amount
                    print(f"Set {category} expense to Rs.{amount}.")
                else:
                    print("Invalid option")
            elif choice == "2":
                print("\nYour Expenses:")
                total = 0
                for category, amount in expenses.items():
                    print(f"{category}: Rs.{amount}")
                    total += amount
                print(f"\nTotal Money Spent = Rs.{total}")

            elif choice == "3":
                print("Exiting program... Have a nice budget!")
                break

            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
    except:
        print('Error please restart the program')
main()