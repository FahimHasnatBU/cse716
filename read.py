import libraries.binary_file_read as binary_file_read
import libraries.record_to_string_convert as record_to_string_convert
from datetime import date, datetime

file = binary_file_read.openFile("data//students")
binary_file_read.jumpToReadingOffset(0, file)
chunk = binary_file_read.readRecord(file)
string = chunk.decode()

relations = {
    "students": [
        {"name": "ID", "type": int},
        {"name": "Name", "type": str},
        {"name": "BirthDate", "type": date},
        {"name": "Address", "type": str}
    ]
}

name_of_relation = input("Which Relation do you want to work on ?\n")

while True:
    record = []
    try:
        chunk = binary_file_read.readRecord(file)
        string = chunk.decode()
        typeList = []
        for i in relations[name_of_relation]:
            typeList.append(i["type"])
        record = record_to_string_convert.retrieveRecordFromString(string, typeList)
        result = ''
        for idx, i in enumerate(record):
            if typeList[idx] == int:
                i = str(i)
            if typeList[idx] == date:
                i = i.strftime('%m/%d/%Y')
            if idx == 0:
                result = i
            else:
                result = result + ','+i
        print(result)
    except:
        break
