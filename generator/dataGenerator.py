# xlsxFileName = input('Enter the xlsx file name: ')
# payloadFile = input('Enter the payload file name: ')
xlsxFileName = "test_data.xlsx"
payloadFile = "eval_payload.txt"

if __name__ == '__main__':
    payload_list = list()
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from xlsxImport.pandasImport import Pandasimport
        from fileUtilities.fileUtility import fileToList
        try:
            userData = Pandasimport.retrieve_xlsx(xlsxFileName)
            payload_list = fileToList.readFileToList(payloadFile)
        except:
            print('Check if {} & {} files exist in dataFolder..'.format(
                xlsxFileName, payloadFile))
    else:
        from ..xlsxImport.pandasImport import Pandasimport
        from ..fileUtilities.fileUtility import fileToList
        try:
            userData = Pandasimport.retrieve_xlsx(xlsxFileName)
            payload_list = fileToList.readFileToList(payloadFile)
        except:
            print('Check if {} & {} files exist in dataFolder..'.format(
                xlsxFileName, payloadFile))

    print(userData['userName'])
    userData
    for entry in payload_list:
        print(entry)
