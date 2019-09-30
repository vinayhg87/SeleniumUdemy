import xlrd

workbook = xlrd.open_workbook("C:\\Users\\VinayVinay\\Desktop\\TestData\\AM GD_July 2019.xlsx")
sheetCount = workbook.nsheets
sheetname = workbook.sheet_names()
print(type(sheetname))
for sh in range (sheetCount):
    worksheet = workbook.sheet_by_name(sheetname[sh])
    nrows = worksheet.nrows
    ncols = worksheet.ncols
    print(nrows, ncols)


