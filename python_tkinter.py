#!/usr/bin/env
# -*- coding: utf-8 -*-

import tkinter

# Create window
window = tkinter.Tk()
window.title('16 Binary Converters')
window.geometry('350x550')

# Create a label to show how to use it
tkinter.Label(window, text='Please enter an integer below,\nand then click the button "Confirm"', font=(
    'Arial', 12), height=2).pack()

# Create an empty label to optimize the layout
tkinter.Label(window, height=1).pack()

# Create an entry and place it
entry = tkinter.Entry(window, show=None)
entry.pack()

# Create an empty label to optimize the layout
tkinter.Label(window, height=1).pack()

# Define the function of the button


def get_number():
    # Get the strings that user type in
    global INPUT_STRING
    INPUT_STRING = entry.get()
    # Check if it's an integer and then set the result
    if INPUT_STRING.isdigit():
        output_string.set(
            f'The 16 binary number of {INPUT_STRING} is {hex(int(INPUT_STRING))}')
        history_listbox.insert(0, [INPUT_STRING, hex(int(INPUT_STRING))])
    elif INPUT_STRING == '':
        output_string.set('')
    else:
        output_string.set(
            'The number you typed in is wrong, \npleace re-enter and click the button "Confirm"')
    # Delete the results that listbox can't show
    history_listbox.delete(20)


# Create a button and bind the function to it
tkinter.Button(window, text='Confirm', command=get_number).pack()

# Create an empty label to optimize the layout
tkinter.Label(window, height=1).pack()

# Create a label to show the result
output_string = tkinter.StringVar()
result_label = tkinter.Label(
    window, textvariable=output_string, font=('Arial', 12), height=2)
result_label.pack()

# Create an empty label to optimize the layout
tkinter.Label(window, height=1).pack()

# Create a listbox to show the results of the most recent calculations
history_listbox = tkinter.Listbox(window, width=55, height=20)
history_listbox.pack()

# THe loop of the window
window.mainloop()
