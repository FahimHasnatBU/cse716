import libraries.binary_file_append as binary_file_append
import libraries.record_to_string_convert as record_to_string_convert
from datetime import datetime, date

relations = {
    "students": [
        {"name": "ID", "type": int},
        {"name": "Name", "type": str},
        {"name": "BirthDate", "type": date},
        {"name": "Address", "type": str}
    ]
}

name_of_relation = input("Which Relation do you want to work on ?\n")


def validateRecord(record):
    recordArr = record.split(",")
    if len(recordArr) != len(relations[name_of_relation]):
        return {"status": False, "message": "Data length mismatch!"}
    else:
        for idx, x in enumerate(recordArr):
            if relations[name_of_relation][idx]["type"] == int:
                try:
                    recordArr[idx] = int(x)
                except:
                    return {"status": False, "message": "Data type mismatch! Expects Integer!"}
            elif relations[name_of_relation][idx]["type"] == date:
                try:
                    recordArr[idx] = datetime.strptime(x, '%m/%d/%Y').date()
                except:
                    return {"status": False, "message": "Data type mismatch! Expects Date (MM/DD/YYYY)!"}
        return {"status": True, "message": "Valid", "data": record_to_string_convert.stringifyRecord(recordArr)}


if name_of_relation in list(relations.keys()):
    while True:
        keyboard = input("Input a record. (Type QUIT to exit)\n")
        if keyboard == "QUIT":
            print("Thank You. Bye!")
            break
        validate = validateRecord(keyboard)
        if not validate["status"]:
            print(validate["message"])
            break
        else:
            f = binary_file_append.createOrOpenFileForAppend("data//students")
            binary_file_append.appendToFile(f, validate["data"] + "******")
            f.close()
else:
    print("Wrong Input!! Type QUIT to exit")

# 22166016,Fahim,03/22/1994,Mohakhali
