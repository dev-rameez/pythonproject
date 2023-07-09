import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pickle

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
        fig = Figure(figsize=(10, 5))

        a = fig.add_subplot(121)
        a.bar(self.expenses.keys(), self.expenses.values())
        a.set_title('Expenses')

        b = fig.add_subplot(122)
        b.bar(self.budgets.keys(), self.budgets.values())
        b.set_title('Budgets')

        return fig

class FinanceTrackerGUI:
    def __init__(self, root):
        self.tracker = FinanceTracker()

        self.root = root
        self.root.title("Finance Tracker")

        # Add income
        self.income_label = tk.Label(root, text="Income:")
        self.income_label.pack()
        self.income_entry = tk.Entry(root)
        self.income_entry.pack()
        self.income_button = tk.Button(root, text="Add Income", command=self.add_income)
        self.income_button.pack()

        # Add expense
        self.expense_label = tk.Label(root, text="Expense:")
        self.expense_label.pack()
        self.expense_entry = tk.Entry(root)
        self.expense_entry.pack()
        self.expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.expense_button.pack()

        # View balance
        self.balance_button = tk.Button(root, text="View Balance", command=self.view_balance)
        self.balance_button.pack()

        # Set savings goal
        self.savings_goal_label = tk.Label(root, text="Savings Goal:")
        self.savings_goal_label.pack()
        self.savings_goal_entry = tk.Entry(root)
        self.savings_goal_entry.pack()
        self.savings_goal_button = tk.Button(root, text="Set Savings Goal", command=self.set_savings_goal)
        self.savings_goal_button.pack()

        # Save money
        self.save_money_label = tk.Label(root, text="Save Money:")
        self.save_money_label.pack()
        self.save_money_entry = tk.Entry(root)
        self.save_money_entry.pack()
        self.save_money_button = tk.Button(root, text="Save Money", command=self.save_money)
        self.save_money_button.pack()

        # View savings progress
        self.savings_progress_button = tk.Button(root, text="View Savings Progress", command=self.view_savings_progress)
        self.savings_progress_button.pack()

        # Visualize data
        self.visualize_button = tk.Button(root, text="Visualize Data", command=self.visualize_data)
        self.visualize_button.pack()

    def add_income(self):
        amount = float(self.income_entry.get())
        self.tracker.add_income(amount)
        messagebox.showinfo("Income", f"Added income: {amount}")

    def add_expense(self):
        amount = float(self.expense_entry.get())
        self.tracker.add_expense("Misc", amount)
        messagebox.showinfo("Expense", f"Added expense: {amount}")

    def view_balance(self):
        balance = self.tracker.get_balance()
        messagebox.showinfo("Balance", f"Current balance: {balance}")

    def set_savings_goal(self):
        amount = float(self.savings_goal_entry.get())
        self.tracker.set_savings_goal(amount)
        messagebox.showinfo("Savings Goal", f"Set savings goal: {amount}")

    def save_money(self):
        amount = float(self.save_money_entry.get())
        self.tracker.save_money(amount)
        messagebox.showinfo("Save Money", f"Saved money: {amount}")

    def view_savings_progress(self):
        progress = self.tracker.get_savings_progress()
        messagebox.showinfo("Savings Progress", f"Savings progress: {progress}")

    def visualize_data(self):
        fig = self.tracker.visualize_data()
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()


def main():
    root = tk.Tk()
    gui = FinanceTrackerGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
