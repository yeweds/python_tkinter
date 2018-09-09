#!/usr/bin/env
# -*- coding: utf-8 -*-
import tkinter
import tkinter.messagebox
import threading
import time


def arrow():
    time.sleep(1)
    while 1:
        if WINDOW_STATUS == 'opening':
            arrow_string.set('==>  =')
            time.sleep(0.2)
            arrow_string.set('==>')
            time.sleep(0.2)
            arrow_string.set('>  ==>')
            time.sleep(0.2)
            arrow_string.set('=>  ==')
            time.sleep(0.2)
        else:
            break


def main():
    threading.Thread(target=arrow).start()


if __name__ == '__main__':
    main()
    # Create main_window
    main_window = tkinter.Tk()
    main_window.title('Binary Converters')
    main_window.geometry('350x470')
    WINDOW_STATUS = 'opening'

    # Create a hidden main_window to copy the result to clipboard
    copy_main_window = tkinter.Tk()
    copy_main_window.withdraw()
    copy_main_window.clipboard_clear()

    # The initial setting of some text of the functions
    CONVERTER_MODE = 16
    function_menu_text = 'Function setting'
    sixteen_binary_text = '16 binary converter'
    eight_binary_text = '8 binary converter'
    two_binary_text = '2 binary converter'
    SUCCESSFUL_OUTPUT_16_1 = 'The 16 binary number of '
    SUCCESSFUL_OUTPUT_16_2 = ' is '
    SUCCESSFUL_OUTPUT_8_1 = 'The 8 binary number of '
    SUCCESSFUL_OUTPUT_8_2 = ' is '
    SUCCESSFUL_OUTPUT_2_1 = 'The 2 binary number of '
    SUCCESSFUL_OUTPUT_2_2 = ' is '
    SUCCESSFUL_OUTPUT_END = '\nThe Result has been copied'
    FAILED_OUTPUT = 'The number you typed in is wrong, \nplease re-enter and click the button "Confirm"'
    FAILED_TITLE = 'Error'

    # Create a menu_bar to change the function and language of this program
    menu_bar = tkinter.Menu(main_window)


    # Create functions for calculation mode and language selection

    def sixteen_binary_converter():
        global CONVERTER_MODE
        CONVERTER_MODE = 16
        output_binary.config(text='16')


    def eight_binary_converter():
        global CONVERTER_MODE
        CONVERTER_MODE = 8
        output_binary.config(text='8')


    def two_binary_converter():
        global CONVERTER_MODE
        CONVERTER_MODE = 2
        output_binary.config(text='2')


    def switch_to_english():
        global SUCCESSFUL_OUTPUT_16_1, SUCCESSFUL_OUTPUT_16_2, SUCCESSFUL_OUTPUT_8_1, SUCCESSFUL_OUTPUT_8_2, \
            SUCCESSFUL_OUTPUT_2_1, SUCCESSFUL_OUTPUT_2_2, SUCCESSFUL_OUTPUT_END, FAILED_OUTPUT, FAILED_TITLE
        main_window.title('Binary Converters')
        explain_label.config(text='Please enter an integer below,\nand then click the button "Confirm"')
        confirm_button.config(text='Confirm')
        SUCCESSFUL_OUTPUT_16_1 = 'The 16 binary number of '
        SUCCESSFUL_OUTPUT_16_2 = ' is '
        SUCCESSFUL_OUTPUT_8_1 = 'The 8 binary number of '
        SUCCESSFUL_OUTPUT_8_2 = ' is '
        SUCCESSFUL_OUTPUT_2_1 = 'The 2 binary number of '
        SUCCESSFUL_OUTPUT_2_2 = ' is '
        SUCCESSFUL_OUTPUT_END = '\nThe Result has been copied'
        FAILED_OUTPUT = 'The number you typed in is wrong, \npleace re-enter and click the button "Confirm"'
        FAILED_TITLE = 'Error'


    def switch_to_chinese():
        global SUCCESSFUL_OUTPUT_16_1, SUCCESSFUL_OUTPUT_16_2, SUCCESSFUL_OUTPUT_8_1, SUCCESSFUL_OUTPUT_8_2, \
            SUCCESSFUL_OUTPUT_2_1, SUCCESSFUL_OUTPUT_2_2, SUCCESSFUL_OUTPUT_END, FAILED_OUTPUT, FAILED_TITLE
        main_window.title('进制转换器')
        explain_label.config(text='请在下方输入需转换整数，并点击“确认”键')
        confirm_button.config(text='确认')
        SUCCESSFUL_OUTPUT_16_1 = ''
        SUCCESSFUL_OUTPUT_16_2 = '的16进制为'
        SUCCESSFUL_OUTPUT_8_1 = ''
        SUCCESSFUL_OUTPUT_8_2 = '的8进制为'
        SUCCESSFUL_OUTPUT_2_1 = ''
        SUCCESSFUL_OUTPUT_2_2 = '的2进制为'
        SUCCESSFUL_OUTPUT_END = '\n结果已被复制'
        FAILED_OUTPUT = '输入有误，请重新输入并点击“确认键”'
        FAILED_TITLE = '错误'


    # Create menu for function and language selection
    function_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=function_menu_text, menu=function_menu)
    function_menu.add_command(label=sixteen_binary_text,
                              command=sixteen_binary_converter)
    function_menu.add_command(label=eight_binary_text,
                              command=eight_binary_converter)
    function_menu.add_command(label=two_binary_text, command=two_binary_converter)
    language_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Language/语言', menu=language_menu)
    language_menu.add_command(label='English', command=switch_to_english)
    language_menu.add_command(label='中文（简体）', command=switch_to_chinese)
    main_window.config(menu=menu_bar)

    # Create a label to show how to use it
    explain_label = tkinter.Label(main_window,
                                  text='Please enter an integer below,\nand then click the button "Confirm"',
                                  font=('Arial', 12), height=2)
    explain_label.place(x=175, y=30, anchor='center')

    # Create two label controls to show the calculation mode
    input_binary = tkinter.Label(main_window, text='10')
    input_binary.place(x=25, y=70, anchor='center')
    arrow_string = tkinter.StringVar()
    tkinter.Label(main_window, textvariable=arrow_string).place(x=55, y=70, anchor='center')
    output_binary = tkinter.Label(main_window, text='16')
    output_binary.place(x=80, y=70, anchor='center')

    # Create an entry and place it
    entry = tkinter.Entry(main_window, show=None)
    entry.place(x=170, y=70, anchor='center')


    # Define the function of the button

    def get_number():
        # Get the strings that user type in
        global INPUT_STRING
        INPUT_STRING = entry.get()
        # Check if it's an integer and then set the result
        if INPUT_STRING.isdigit():
            if CONVERTER_MODE == 16:
                output_string.set(SUCCESSFUL_OUTPUT_16_1 + INPUT_STRING + SUCCESSFUL_OUTPUT_16_2 + hex(
                    int(INPUT_STRING)) + SUCCESSFUL_OUTPUT_END)
                history_listbox.insert(0, [INPUT_STRING, hex(int(INPUT_STRING))])
                copy_main_window.clipboard_clear()
                main_window.clipboard_append(hex(int(INPUT_STRING)))
            elif CONVERTER_MODE == 8:
                output_string.set(SUCCESSFUL_OUTPUT_8_1 + INPUT_STRING + SUCCESSFUL_OUTPUT_8_2 + oct(
                    int(INPUT_STRING)) + SUCCESSFUL_OUTPUT_END)
                history_listbox.insert(0, [INPUT_STRING, oct(int(INPUT_STRING))])
                main_window.clipboard_append(oct(int(INPUT_STRING)))
            else:
                output_string.set(SUCCESSFUL_OUTPUT_2_1 + INPUT_STRING + SUCCESSFUL_OUTPUT_2_2 + bin(
                    int(INPUT_STRING)) + SUCCESSFUL_OUTPUT_END)
                history_listbox.insert(0, [INPUT_STRING, bin(int(INPUT_STRING))])
                main_window.clipboard_append(bin(int(INPUT_STRING)))
        elif INPUT_STRING == '':
            output_string.set('')
        else:
            tkinter.messagebox.showerror(title=FAILED_TITLE, message=FAILED_OUTPUT)
        # Delete the results that listbox can't show
        history_listbox.delete(20)


    # Create a button and bind the function to it
    confirm_button = tkinter.Button(main_window, text='Confirm', command=get_number)
    confirm_button.place(x=270, y=70, anchor='center')

    # Create a label to show the result
    output_string = tkinter.StringVar()
    result_label = tkinter.Label(main_window, textvariable=output_string, font=('Arial', 12))
    result_label.place(x=175, y=110, anchor='center')

    # Create a listbox to show the results of the most recent calculations
    history_listbox = tkinter.Listbox(main_window, width=55, height=20)
    history_listbox.place(x=175, y=300, anchor='center')

    # The loop of the main_window
    main_window.mainloop()
    print('window has been closed')
