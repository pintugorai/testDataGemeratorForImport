# xlsxFileName = input('Enter the xlsx file name: ')
# payloadFile = input('Enter the payload file name: ')
import random
xlsxFileName = "test_data.xlsx"
payloadFile = "eval_payload.txt"
propertyFile = "properties.xlsx"
payload_list = list()

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from xlsxImport.pandasImport import Pandasimport
        from xlsxImport.pandasexport import Pandasexport
        from fileUtilities.fileUtility import fileToList
        try:
            testData = Pandasimport.retrieve_xlsx(xlsxFileName)
            propertyData = Pandasimport.retrieve_xlsx(propertyFile)
            payload_list = fileToList.readFileToList(payloadFile)
        except:
            print('Check if {} ,{} & {} files exist in dataFolder..'.format(
                xlsxFileName, propertyData, payloadFile))
else:
    from ..xlsxImport.pandasImport import Pandasimport
    from xlsxImport.pandasexport import Pandasexport
    from ..fileUtilities.fileUtility import fileToList
    try:
        testData = Pandasimport.retrieve_xlsx(xlsxFileName)
        propertyData = Pandasimport.retrieve_xlsx(propertyFile)
        payload_list = fileToList.readFileToList(payloadFile)
    except:
        print('Check if {}, {} & {} files exist in dataFolder..'.format(
            xlsxFileName, propertyData, payloadFile))

# print(testData['userName'])
# for i in range(len(payload_list)):
#     print(random.choice(payload_list))
print(propertyData)

for ind in propertyData.index:
    if propertyData['header'][ind] in testData.columns:
        if propertyData['action'][ind] == 'append':
            testData[propertyData['header'][ind]] = testData[propertyData['header'][ind]].apply(
                lambda x: str(x) + random.choice(payload_list))
        elif propertyData['action'][ind] == 'replace':
            testData[propertyData['header'][ind]] = testData[propertyData['header'][ind]].apply(
                lambda x: random.choice(payload_list))

Pandasexport.export_xlsx(testData)
