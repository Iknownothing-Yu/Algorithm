import csv
import codecs

def readSheet(path, sheetName):
    workBook = xlrd.open_workbook(path)
    sheet = workBook.sheet_by_name(sheetName)
    return sheet

def xlsx_to_csv(locatePath, name):
    xlsxFile = readSheet(locatePath, name)
    with codecs.open('D:\pycharm-space\other_files\list2.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for i in range(xlsxFile.nrows):
            rowValue = xlsxFile.cell_value(i, 0) #only get the values of 0 col
            write.writerow(rowValue)

productName = input('the wanted producte is :')
xlsx_to_csv('D:\pycharm-space\other_files\list1.xlsx', productName)
