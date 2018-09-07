#!/usr/bin/env
# -*- coding: utf-8 -*-

import tkinter

# Create window
window = tkinter.Tk()
window.title('Binary Converters')
window.geometry('350x480')

# The initiao setting of some text of the functions
CONVERTER_MODE = 16
FUNCTION_MENU_TEXT = 'Function setting'
SIXTEEN_BINARY_TEXT = '16 binary converter'
EIGHT_BINARY_TEXT = '8 binary converter'
TWO_BINARY_TEXT = '2 binary converter'
SUCCESSFUL_OUTPUT_16_1 = 'The 16 binary number of '
SUCCESSFUL_OUTPUT_16_2 = ' is '
SUCCESSFUL_OUTPUT_8_1 = 'The 8 binary number of '
SUCCESSFUL_OUTPUT_8_2 = ' is '
SUCCESSFUL_OUTPUT_2_1 = 'The 2 binary number of '
SUCCESSFUL_OUTPUT_2_2 = ' is '
FAILED_OUTPUT = 'The number you typed in is wrong, \npleace re-enter and click the button "Confirm"'

# Create a menubar to change the function and language of this program
menubar = tkinter.Menu(window)

# Create functions for function and language selection


def sixteen_binary_converter():
    global CONVERTER_MODE
    CONVERTER_MODE = 16


def eight_binary_converter():
    global CONVERTER_MODE
    CONVERTER_MODE = 8


def two_binary_converter():
    global CONVERTER_MODE
    CONVERTER_MODE = 2


def switch_to_english():
    global SUCCESSFUL_OUTPUT_16_1, SUCCESSFUL_OUTPUT_16_2, SUCCESSFUL_OUTPUT_8_1, SUCCESSFUL_OUTPUT_8_2, SUCCESSFUL_OUTPUT_2_1, SUCCESSFUL_OUTPUT_2_2, FAILED_OUTPUT
    window.title('Binary Converters')
    explain_label.config(
        text='Please enter an integer below,\nand then click the button "Confirm"')
    confirm_button.config(text='Confirm')
    SUCCESSFUL_OUTPUT_16_1 = 'The 16 binary number of '
    SUCCESSFUL_OUTPUT_16_2 = ' is '
    SUCCESSFUL_OUTPUT_8_1 = 'The 8 binary number of '
    SUCCESSFUL_OUTPUT_8_2 = ' is '
    SUCCESSFUL_OUTPUT_2_1 = 'The 2 binary number of '
    SUCCESSFUL_OUTPUT_2_2 = ' is '
    FAILED_OUTPUT = 'The number you typed in is wrong, \npleace re-enter and click the button "Confirm"'


def switch_to_chinese():
    global SUCCESSFUL_OUTPUT_16_1, SUCCESSFUL_OUTPUT_16_2, SUCCESSFUL_OUTPUT_8_1, SUCCESSFUL_OUTPUT_8_2, SUCCESSFUL_OUTPUT_2_1, SUCCESSFUL_OUTPUT_2_2, FAILED_OUTPUT
    window.title('进制转换器')
    explain_label.config(text='请在下方输入需转换整数，并点击“确认”键')
    confirm_button.config(text='确认')
    SUCCESSFUL_OUTPUT_16_1 = ''
    SUCCESSFUL_OUTPUT_16_2 = '的16进制为'
    SUCCESSFUL_OUTPUT_8_1 = ''
    SUCCESSFUL_OUTPUT_8_2 = '的8进制为'
    SUCCESSFUL_OUTPUT_2_1 = ''
    SUCCESSFUL_OUTPUT_2_2 = '的2进制为'
    FAILED_OUTPUT = '输入有误，请重新输入并点击“确认键”'


# Create menu for function and language selection
function_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label=FUNCTION_MENU_TEXT, menu=function_menu)
function_menu.add_command(label=SIXTEEN_BINARY_TEXT,
                          command=sixteen_binary_converter)
function_menu.add_command(label=EIGHT_BINARY_TEXT,
                          command=eight_binary_converter)
function_menu.add_command(label=TWO_BINARY_TEXT, command=two_binary_converter)
language_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Language/语言', menu=language_menu)
language_menu.add_command(label='English', command=switch_to_english)
language_menu.add_command(label='中文（简体）', command=switch_to_chinese)
window.config(menu=menubar)

# Create a label to show how to use it
explain_label = tkinter.Label(
    window, text='Please enter an integer below,\nand then click the button "Confirm"', font=('Arial', 12), height=2)
explain_label.place(x=175, y=30, anchor='center')

# Create an entry and place it
entry = tkinter.Entry(window, show=None)
entry.place(x=140, y=70, anchor='center')

# Define the function of the button


def get_number():
    # Get the strings that user type in
    global INPUT_STRING
    INPUT_STRING = entry.get()
    # Check if it's an integer and then set the result
    if INPUT_STRING.isdigit():
        if CONVERTER_MODE == 16:
            output_string.set(SUCCESSFUL_OUTPUT_16_1+INPUT_STRING +
                              SUCCESSFUL_OUTPUT_16_2+hex(int(INPUT_STRING)))
            history_listbox.insert(0, [INPUT_STRING, hex(int(INPUT_STRING))])
        elif CONVERTER_MODE == 8:
            output_string.set(SUCCESSFUL_OUTPUT_8_1+INPUT_STRING +
                              SUCCESSFUL_OUTPUT_8_2+oct(int(INPUT_STRING)))
            history_listbox.insert(0, [INPUT_STRING, oct(int(INPUT_STRING))])
        else:
            output_string.set(SUCCESSFUL_OUTPUT_2_1+INPUT_STRING +
                              SUCCESSFUL_OUTPUT_2_2+bin(int(INPUT_STRING)))
            history_listbox.insert(0, [INPUT_STRING, bin(int(INPUT_STRING))])
    elif INPUT_STRING == '':
        output_string.set('')
    else:
        output_string.set(FAILED_OUTPUT)
    # Delete the results that listbox can't show
    history_listbox.delete(20)


# Create a button and bind the function to it
confirm_button = tkinter.Button(window, text='Confirm', command=get_number)
confirm_button.place(x=240, y=70, anchor='center')

# Create a label to show the result
output_string = tkinter.StringVar()
result_label = tkinter.Label(
    window, textvariable=output_string, font=('Arial', 12), height=2)
result_label.place(x=175, y=125, anchor='center')

# Create a listbox to show the results of the most recent calculations
history_listbox = tkinter.Listbox(window, width=55, height=20)
history_listbox.place(x=175, y=310, anchor='center')

# THe loop of the window
window.mainloop()
