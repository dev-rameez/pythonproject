import tkinter as tk
from tkinter import messagebox
from project import FinanceTracker

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

def main():
    root = tk.Tk()
    gui = FinanceTrackerGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
