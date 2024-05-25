# Importing necessary libraries
from tkinter import *

# Function to calculate number of words in a string
def get_word_count(string: str):

    # String preprocessing
    string = string.strip()
    string = string.split()

    word_count = len(string)
    
    # Return word count
    return word_count


# Function to be called on modification of user entry
def on_text_change(event):

    text_area.edit_modified(False)

    # Get user input
    string = str(text_area.get(1.0, END))

    # Get word count
    word_count = get_word_count(string)
    
    # Display word count
    output_entry.delete(0, END)
    output_entry.insert(0, word_count)


# Creating the master window
window = Tk()

# Label for prompting user to enter input
entry_label = Label(window, text = "Enter a sentence or a paragraph")
entry_label.pack()

# Text entry for user input
text_area = Text(window)
text_area.pack()

# Calling on_text_change on modification of user entry
text_area.bind("<<Modified>>", on_text_change)


output_label = Label(window, text = "Number of words")
output_label.pack()

# Entry for displaying number of words
output_entry = Entry(window)
output_entry.pack()

window.mainloop()