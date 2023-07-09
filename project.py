import pickle
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.budgets = {}
        self.savings_goal = 0
        self.savings = 0

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, category, amount):
        if category not in self.expenses:
            self.expenses[category] = 0
        self.expenses[category] += amount

    def set_budget(self, category, amount):
        self.budgets[category] = amount

    def set_savings_goal(self, amount):
        self.savings_goal = amount

    def save_money(self, amount):
        self.savings += amount

    def get_balance(self):
        return self.income - sum(self.expenses.values())

    def get_budget_progress(self, category):
        return self.expenses.get(category, 0) / self.budgets.get(category, 1)

    def get_savings_progress(self):
        return self.savings / self.savings_goal

    def visualize_data(self):
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.bar(self.expenses.keys(), self.expenses.values())
        plt.title('Expenses')

        plt.subplot(1, 2, 2)
        plt.bar(self.budgets.keys(), self.budgets.values())
        plt.title('Budgets')

        plt.show()

def load_data():
    try:
        with open('data.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return FinanceTracker()

def save_data(tracker):
    with open('data.pkl', 'wb') as f:
        pickle.dump(tracker, f)

def main():
    tracker = load_data()

    while True:
        print("1. Add income")
        print("2. Add expense")
        print("3. Set budget")
        print("4. Set savings goal")
        print("5. Save money")
        print("6. Check balance")
        print("7. Check budget progress")
        print("8. Check savings progress")
        print("9. Visualize data")
        print("0. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            amount = float(input("Enter income amount: "))
            tracker.add_income(amount)
        elif choice == 2:
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(category, amount)
        elif choice == 3:
            category = input("Enter budget category: ")
            amount = float(input("Enter budget amount: "))
            tracker.set_budget(category, amount)
        elif choice == 4:
            amount = float(input("Enter savings goal: "))
            tracker.set_savings_goal(amount)
        elif choice == 5:
            amount = float(input("Enter amount to save: "))
            tracker.save_money(amount)
        elif choice == 6:
            print("Current balance: ", tracker.get_balance())
        elif choice == 7:
            category = input("Enter budget category: ")
            print("Budget progress: ", tracker.get_budget_progress(category))
        elif choice == 8:
            print("Savings progress: ", tracker.get_savings_progress())
        elif choice == 9:
            tracker.visualize_data()
        elif choice == 0:
            break

    save_data(tracker)

if __name__ == '__main__':
    main()