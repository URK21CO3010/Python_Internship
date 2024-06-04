import time
import tkinter
from tkinter import messagebox

expenses = []


def process_input():

    # Amount input validation
    amount = str(amount_entry.get())
    if not amount.isdigit() or int(amount) == 0:
        messagebox.showwarning(title = "Invalid amount", message = "Amount should be a positive integer")
        return

    amount = int(amount)
    

    # Category input validation
    category = category_value.get()
    if category == 'None':
        messagebox.showwarning(title = "Category not selected", message = "Please select one of the available categories")
        return


    # Get description (optional input)
    description = description_entry.get()

    add_expense(amount = amount, category = category, description = description, time = time.localtime())



def add_expense(amount, category, description, time):

    expense = {
        'amount': amount,
        'category': category,
        'description': description,
        'time': time
    }

    expenses.append(expense)


def display_expenses():

    expenses_string = ""

    
    for expense in expenses:

        amount = str(expense['amount'])
        category = str(expense['category']).capitalize()
        description = str(expense['description'])

        year, month, day, hour, minute, *_ = expense['time']

        date = str(day) + '.' + str(month) + '.' + str(year)
        time = str(hour) + ':' + str(minute)

        expenses_string += f"Rs.{amount} - {category} - {date} {time} ({description})\n\n"
    
    view_area.delete(1.0, tkinter.END)
    view_area.insert(1.0, expenses_string)


window = tkinter.Tk()

amount_label = tkinter.Label(master = window, text = "Amount spent:")
amount_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "e")

amount_entry = tkinter.Entry(master = window)
amount_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

category_value = tkinter.StringVar(value = 'None')

category_frame = tkinter.LabelFrame(master = window, text = "Category")
category_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "w")

category1 = tkinter.Radiobutton(master = category_frame, text = 'Food', variable = category_value, value = 'food')
category1.grid(row = 0, column = 0, padx = 5, pady = 5)

category2 = tkinter.Radiobutton(master = category_frame, text = 'Transportation', variable = category_value, value = 'transport')
category2.grid(row = 0, column = 1, padx = 5, pady = 5)

category3 = tkinter.Radiobutton(master = category_frame, text = 'Entertainment', variable = category_value, value = 'entertainment')
category3.grid(row = 0, column = 2, padx = 5, pady = 5)

category4 = tkinter.Radiobutton(master = category_frame, text = 'Housing and Utilities', variable = category_value, value = 'housing_and_utilities')
category4.grid(row = 0, column = 3, padx = 5, pady = 5)

category5 = tkinter.Radiobutton(master = category_frame, text = 'Miscellaneous', variable = category_value, value = 'miscellaneous')
category5.grid(row = 0, column = 4, padx = 5, pady = 5)

description_label = tkinter.Label(master = window, text = "Description:")
description_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "e")

description_entry = tkinter.Entry(master = window, width = 30)
description_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

add_expense_button = tkinter.Button(master = window, text = "Add", command = process_input)
add_expense_button.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)

view_expenses_button = tkinter.Button(master = window, text = "View Expenses", command = display_expenses)
view_expenses_button.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)

view_area = tkinter.Text(master = window, height = 10, width = 50)
view_area.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10)

window.mainloop()
