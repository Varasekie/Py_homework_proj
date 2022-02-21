import xlrd

path = './材料1.xlsx'
dict_key = {}
data = xlrd.open_workbook(path, 'rb')
table = data.sheet_by_index(0)
colAmount = table.ncols
rowAmount = table.nrows

count = 1
rowIndex = 1
while rowIndex < rowAmount:
    filename = '结果' + str(count)+'.txt'
    count = count + 1
    with open(filename, 'w') as f:
        for r in range(rowIndex, min(rowIndex + 10, rowAmount)):
            ID = table.cell_value(rowIndex, 0)
            name = table.cell_value(rowIndex, 1)
            keyword = table.cell_value(rowIndex, 2)
            journey = table.cell_value(rowIndex, 3)
            f.write('【论文ID】' + ID + '\n')
            f.write('【论文篇名】' + name + '\n')
            f.write('【关键词】' + keyword + '\n')
            f.write('【期刊】' + journey + '\n')
            f.write('-------------------------' + '\n')
    rowIndex = rowIndex + 10
