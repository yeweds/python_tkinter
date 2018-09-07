#!/usr/bin/env
# -*- coding: utf-8 -*-

import tkinter

# Create window
window = tkinter.Tk()
window.title('Binary Converters')
window.geometry('350x560')

# The setting of some text of the function "get_number()"
SUCCESSFUL_OUTPUT_1 = 'The 16 binary number of '
SUCCESSFUL_OUTPUT_2 = ' is '
FAILED_OUTPUT = 'The number you typed in is wrong, \npleace re-enter and click the button "Confirm"'

# Create a function for Radiobuttons


def language_setting():
    global SUCCESSFUL_OUTPUT_1, SUCCESSFUL_OUTPUT_2, FAILED_OUTPUT
    language_selection_label.config(
        text=f'(You have selected {language_variable.get()} for this program)')
    if language_variable.get() == 'chinese':
        window.title('进制转换器')
        explain_label.config(text='请在下方输入需转换整数，并点击“确认”键')
        confirm_button.config(text='确认')
        SUCCESSFUL_OUTPUT_1 = ''
        SUCCESSFUL_OUTPUT_2 = '的16进制为'
        FAILED_OUTPUT = '输入有误，请重新输入并点击“确认键”'
    else:
        window.title('Binary Converters')
        explain_label.config(
            text='Please enter an integer below,\nand then click the button "Confirm"')
        confirm_button.config(text='Confirm')
        SUCCESSFUL_OUTPUT_1 = 'The 16 binary number of '
        SUCCESSFUL_OUTPUT_2 = ' is '
        FAILED_OUTPUT = 'The number you typed in is wrong, \npleace re-enter and click the button "Confirm"'


# Create a Radiobutton to set the language
language_variable = tkinter.StringVar()
tkinter.Radiobutton(window, text='English', variable=language_variable,
                    value='english', command=language_setting).place(x=0, y=0, anchor='nw')
tkinter.Radiobutton(window, text='中文（简体）', variable=language_variable,
                    value='chinese', command=language_setting).place(x=0, y=30, anchor='nw')

# Create a label to show the language selection
language_selection_label = tkinter.Label(
    window, text='(You have not selected any language yet!)')
language_selection_label.place(x=100, y=15, anchor='nw')

# Create a label to show how to use it
explain_label = tkinter.Label(
    window, text='Please enter an integer below,\nand then click the button "Confirm"', font=('Arial', 12), height=2)
explain_label.place(x=175, y=110, anchor='center')

# Create an entry and place it
entry = tkinter.Entry(window, show=None)
entry.place(x=140, y=150, anchor='center')

# Define the function of the button


def get_number():
    # Get the strings that user type in
    global INPUT_STRING
    INPUT_STRING = entry.get()
    # Check if it's an integer and then set the result
    if INPUT_STRING.isdigit():
        output_string.set(SUCCESSFUL_OUTPUT_1+INPUT_STRING +
                          SUCCESSFUL_OUTPUT_2+hex(int(INPUT_STRING)))
        history_listbox.insert(0, [INPUT_STRING, hex(int(INPUT_STRING))])
    elif INPUT_STRING == '':
        output_string.set('')
    else:
        output_string.set(FAILED_OUTPUT)
    # Delete the results that listbox can't show
    history_listbox.delete(20)


# Create a button and bind the function to it
confirm_button = tkinter.Button(window, text='Confirm', command=get_number)
confirm_button.place(x=240, y=150, anchor='center')

# Create a label to show the result
output_string = tkinter.StringVar()
result_label = tkinter.Label(
    window, textvariable=output_string, font=('Arial', 12), height=2)
result_label.place(x=175, y=205, anchor='center')

# Create a listbox to show the results of the most recent calculations
history_listbox = tkinter.Listbox(window, width=55, height=20)
history_listbox.place(x=175, y=390, anchor='center')

# THe loop of the window
window.mainloop()
