import xlsxwriter

#create a workbook and add a worksheet
workbook = xlsxwriter.Workbook('MarExpenses.xlsx')
worksheet = workbook.add_worksheet()

#some data to be written in the worksheet
expenses = (
    ['Rent', 20000],
    ['electricity', 5000],
    ['Food', 3000],
    ['Maid', 5000],
)

#Start from first cell. Rows and columns are zero indexed
row = 0
col = 0

#Iterate over the data and write it out row by row
for item, cost in (expenses):
    worksheet.write(row, col,  item)
    worksheet.write(row,col+1,  cost)
    row += 1

#Write a total using a formula
worksheet.write(row, 0, 'Total')
worksheet.write(row,1, '=SUM(B1:B4)')


workbook.close()