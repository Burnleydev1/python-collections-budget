from . import Expense


class BudgetList:


    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):

        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            item += self.sum_expenses

        else:
            self.overages.append(item)
            item += self.sum_expenses

    def __len__(self):
        len(self.sum_expenses) + len(self.overages)

def main():
    myBudgetList = BudgetList(1200)

    expenses = Expense.Expenses()
    expenses.read_expenses("data/spending_.csv")

    for expense in expenses.list:
        myBudgetList.append(expense.amount)
    print(f'The count of all expenses: {str(len(myBudgetList))}')