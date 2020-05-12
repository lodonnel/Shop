import tkinter as tk
from doctest import master
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.simpledialog import *
from prettytable import PrettyTable
from tkintertable import TableCanvas, TableModel


root = tkinter.Tk()  # setup graphic root
root.withdraw()  # hide initial window


def init():
    w = 300
    h = 200
    x = 0
    y = 0

    # Gets both half the screen width/height and window width/height

    position_right = int(root.winfo_screenwidth()/2 - w/2)
    position_down = int(root.winfo_screenheight()/2 - h/2)
    root.geometry("+{}+{}".format(position_right, position_down))

    print(f'Width:{position_right} Height:{position_down} w:{w} h:{h} x:{x} y:{y}')
    root.focus_set()


def show_message(title, message):
    init()
    answer = askstring(title, message)
    return answer


def message_box(message):
    messagebox.showwarning("Error", message)


def table_to_console(header, item_list):
    x = PrettyTable()
    x.field_names = header

    for item in item_list:
        x.add_row(item)
    print(x)
    table_gui()


def table_gui(data):
    tframe = Frame(master)
    tframe.pack()
    table = TableCanvas(tframe)
    table.show()


#if __name__ == '__main__': main()