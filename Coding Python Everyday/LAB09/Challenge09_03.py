# 딕셔너리 합치기
def sum_dictionary(*items):
    output_dict = {}
    for item in items:
        for key in item:
            if key in output_dict:
                if not isinstance(output_dict[key],list):
                    output_dict[key] = [output_dict[key]]
                output_dict[key].append(item[key])
            else:
                output_dict[key] = item[key]
    return output_dict

dict_01 = {
    "key": "value1",
    "key2": "value2",
    "the key": "the value1"
}
dict_02 = {
    "key3": "value3",
    "key4": "value4",
    "the key": "the value2"
}
dict_03 = {
    "key5": "value5",
    "key6": "value6"
}

print(sum_dictionary(dict_01, dict_02, dict_03))