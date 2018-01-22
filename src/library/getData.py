import csv
from src.library.getRootPath import getRootPath

def getDataFromCsv(filepath):
    filepath = getRootPath() + file
    all_test_data = []
    with open(filepath) as filedata:
        # print(filedata)
        filereader = csv.reader(filedata)
        # print(filereader)

        next(filereader)   # 去掉第一行数据 ['username', 'passwd', 'repasswd', 'email']
        for row in filereader:
            # print(row)
            all_test_data.append(row)


    return all_test_data
file = "/src/data/test_data.csv"
print(getDataFromCsv(file))