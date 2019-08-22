import os
try:
    import pandas as pd
    import xlrd
except:
    os.system('pip install pandas')
    os.system('pip install xlrd')
    import pandas as pd
    import xlrd


class Pandasimport:
    def retrieve_xlsx(xlsxFileName):
        current_file = os.path.abspath(os.path.dirname(__file__))
        excelPath = os.path.join(current_file, '../dataFolder/', xlsxFileName)
        user_xlsx = pd.ExcelFile(excelPath)
        user_data = pd.read_excel(
            user_xlsx, 'Sheet1', index_col=None, na_values=['NA'])
        return user_data
