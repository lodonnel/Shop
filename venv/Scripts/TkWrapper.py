# from tkinter import *
# import tkinter
#
#
# def get_rows(data):
#     return len(data)
#
#
# def get_columns(data):
#     row = data.pop()
#     return len(row)
#
#
# def get_headers(header):
#     pass
#
#
# class TkWrapper(tkinter):
#
#     root = Tk()
#
#     def fill(self, rows, columns, data):
#         pass
#
#     def edit_cell(self, row, column):
#         pass
#
#     def edit_record(self, row):
#         pass
#
#     def table(self, header, data):
#         rows = get_rows(data)
#         cols = get_columns(data)
#
#         # change data to array of arrays
#         headers = []    # = top row of sheet
#         row = []
#         sheet = []
#
#         headers = header
#         sheet[0] = headers
#
#         for row_list in data:
#             row = []
#             for k,v in row_list:
#                 row.append = v
#             sheet.append(row)
#
#         self.fill(rows, cols, data)
#         for i in rows:
#             for j in cols:
#                 pass
#
#         mainloop()
#
#
