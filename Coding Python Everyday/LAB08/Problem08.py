# 처음과 마지막 요소 추출
def firstlast(iterable):
    if type(iterable) is str:
        return f"{iterable[0]}{iterable[-1]}"
    if type(iterable) is list:
        return [iterable[0], iterable[-1]]
    else:
        return iterable[0], iterable[-1] 

print(firstlast("abc"))
print(firstlast([1,2,3,4]))