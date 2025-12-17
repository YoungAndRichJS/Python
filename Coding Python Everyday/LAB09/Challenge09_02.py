# 정수 변환 가능한 것만 더하기
def sum_numeric(*args):
    output = 0
    for item in args:
        if isinstance(item, int):
            output += item
        else:
            try:
                output += int(item)
            except:
                pass
    return output
            
print(sum_numeric(10, 20, "a", "30", "bcd")) # return 60