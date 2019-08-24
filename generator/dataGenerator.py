import random


class DataGenerator:
    def payloadXlsxGenerator(testData, propertyData, payload_list):
        for ind in propertyData.index:
            if propertyData['header'][ind] in testData.columns:
                if propertyData['action'][ind] == 'append':
                    testData[propertyData['header'][ind]] = testData[propertyData['header'][ind]].apply(
                        lambda x: str(x) + random.choice(payload_list))
                elif propertyData['action'][ind] == 'replace':
                    testData[propertyData['header'][ind]] = testData[propertyData['header'][ind]].apply(
                        lambda x: random.choice(payload_list))
        return testData
