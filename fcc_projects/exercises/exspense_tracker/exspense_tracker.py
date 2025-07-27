#defining a function named add_expense that takes three parameters: expenses, amount and category

```python
def add_expense(expenses , amount , category):

# Create a dictionary with a key 'amount' and value of the amount parameter and pass your new dictionary to the .append() call.
    # add dictonary for category
    
    expenses.append({'amount': amount , 'category': category})

#define a function named print_expenses that takes one parameter expenses.

def print_expenses(expenses):
    for expense in expenses:
     print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')



test = lambda x: x * 2
print(list(map(test, [2, 3, 5, 8])))


#Create expenses list    
expenses = []
