import os


class fileToList:
    def readFileToList(file):
        current_file = os.path.abspath(os.path.dirname(__file__))
        payload_path = os.path.join(current_file, '../dataFolder/', file)
        payload_file = open(payload_path, "r")
        payload_list = list()
        for line in payload_file:
            payload_list.append(line)

        payload_file.close()
        return payload_list
