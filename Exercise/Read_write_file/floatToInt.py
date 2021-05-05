import xlrd
import csv
import codecs

def readSheet(path):
    workBook = xlrd.open_workbook(path)
    sheet = workBook.sheet_by_name('second')
    return sheet

def xlsx_to_csv(locatePath):
    xlsxFile = readSheet(locatePath)
    with codecs.open('D:\pycharm-space\other_files\list2.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for i in range(xlsxFile.nrows):
            rowValue = xlsxFile.row_values(i)
            finalVal = [int(ele) for ele in rowValue] # the integer numbers read from xslx are float, change them first to In
            print(finalVal)
            write.writerow(finalVal)

xlsx_to_csv('D:\pycharm-space\other_files\list1.xlsx')