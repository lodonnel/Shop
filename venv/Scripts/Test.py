# from tkintertable import TableCanvas, TableModel
import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd

# from tkintertable.Testing import sampledata
# from TkWrapper import TkWrapper

#
# class Item:
#     pass
#
#
# class Food(Item):
#     pass
#
#
# class Drink(Item):
#     pass


# tk = TkWrapper()


def main():
    cols = ()
    title = "Stock List"
    header = ('Row No', 'Name',  'Price', 'Stock', 'Size/Weight')
    data = [{'name': 'Coke',  'price': '1.0', 'stock': '10', 'size': '500'},
            {'name': 'Milk', 'price': '2.0', 'stock': '20', 'size': '1000'},
            {'name': '7-UP',  'price': '3.0', 'stock': '30', 'size': '1750'},
            {'name': 'Water', 'price': '4.0', 'stock': '40', 'size': '2000'},
            ]

    # using pandas to convert from dicts to arrays
    df = pd.DataFrame(data)
    vals = df.values

    array = vals.__array__()

    print(array)

    def show():

        cols = header

        tempList = array
        #tempList.sort(key=lambda e: e[1], reverse=True)

        for i, (name, price,stock, size) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(i, name, price, stock, size))

    scores = tk.Tk()

    label = tk.Label(scores, text=title, font=("Arial", 30)).grid(row=0, columnspan=3)

    # create Treeview with 3 columns
    cols = header   # ('Position', 'Name', 'Score')
    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    # set column headings

    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=3)

    showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
    closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

    scores.mainloop()


if __name__ == '__main__': main()
