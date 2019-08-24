from fileUtilities.fileUtility import fileToList
from xlsxIO.pandasIO import PandasIO
from generator.dataGenerator import DataGenerator

xlsxFileName = "test_data.xlsx"
payloadFile = "eval_payload.txt"
propertyFile = "properties.xlsx"
# xlsxFileName = input('Enter the xlsx file name: ')
# payloadFile = input('Enter the payload file name: ')
try:
    testData = PandasIO.retrieve_xlsx(xlsxFileName)
    propertyData = PandasIO.retrieve_xlsx(propertyFile)
    payload_list = fileToList.readFileToList(payloadFile)
except:
    print('Check if {} ,{} & {} files exist in dataFolder..'.format(
        xlsxFileName, propertyData, payloadFile))
finally:
    xlsxOutput = DataGenerator.payloadXlsxGenerator(
        testData, propertyData, payload_list)
    PandasIO.export_xlsx(xlsxOutput)
