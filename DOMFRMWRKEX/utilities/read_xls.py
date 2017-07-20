import xlrd
# #open a workbook
# wb=xlrd.open_workbook('my_xl.xlsx')
# #open a worksheet_by_index
# ws=wb.sheet_by_index(0)
# #open a worksheet by name
# ws1=wb.sheet_by_name('Sheet1')
# #Get the name of the sheet
# ws1_name=ws1.name
# print(ws1_name)
# #Read the data from the cell
# cell0_0=ws1.cell(0,0).value
# print(cell0_0)
# cell0_1=ws1.cell(0,1).value
# print(cell0_1)
# #  To check the number of sheets
# no_sheets=wb.nsheets
# print(no_sheets)
#
# # To get the name os the sheets
# names_sheet=wb.sheet_names()
# print(names_sheet)
#
# #To find the total number of rows and columns in the sheet WS.NROWS,WS.NCOLS
# print("{} has {} rows and {} columns".format(ws1.name,ws1.nrows,ws1.ncols))
#
# # to read data from rows
# xl_read=[]
# for row in range(1,ws1.nrows):
#     for col in range(1,ws1.ncols):
#         cell_value=ws1.cell(row,col).value
#         xl_read.append(cell_value)
#     print(xl_read)
#     xl_read.clear()


def read_xl(file_name,sheet_name):
    xl_rows_copy=[]
    xl_table=[]
    wb = xlrd.open_workbook(file_name)
    ws = wb.sheet_by_name(sheet_name)
    xl_rows = []
    for row in range(1, ws.nrows):
        for col in range(1, ws.ncols):
            cell_value = ws.cell(row, col).value
            if type(cell_value)is float:
                cell_value=int(cell_value)
            cell_value=str(cell_value)
            xl_rows.append(cell_value)
        xl_rows_copy=xl_rows.copy()
        xl_rows.clear()
        xl_table.append(xl_rows_copy)
    return xl_table
#
# def get_xl_data(file_name,sheet_name):
#     xl_data=read_xl(file_name,sheet_name)
#     for row in range(len(xl_data)):
#         return xl_data[row]
#
# print(get_xl_data('my_xl.xlsx','Sheet1'))
# print(read_xl('my_xl.xlsx','Sheet1'))

