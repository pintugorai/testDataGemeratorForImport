import os
try:
    import pandas as pd
    import xlrd
except:
    os.system('pip install pandas')
    os.system('pip install xlrd')
    import pandas as pd
    import xlrd


class Pandasexport:
    def export_xlsx(xlsxDataFrame):
        current_file = os.path.abspath(os.path.dirname(__file__))
        exportPath = os.path.join(current_file, '../dataFolder/output.xlsx')
        xlsxDataFrame.to_excel(exportPath, sheet_name='Sheet_name_1')
