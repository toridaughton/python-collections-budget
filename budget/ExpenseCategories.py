from . import Expense
import matplotlib.pyplot as plt

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()
    if(divided_set_comp != divided_for_loop):
        print("Sets are NOT equal by == test")
    for d_loop, set_comp in zip(divided_for_loop, divided_set_comp):
        if not (d_loop.issubset(set_comp) and set_comp.issubset(d_loop)):
            print("Sets are NOT equal by supbset test")

if __name__ == "__main__":
    main()