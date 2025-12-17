# 처음과 마지막 요소 추출
def firstlast(sequence):
    return sequence[:1] + sequence[-1:]

print(firstlast("abcd"))
print(firstlast([1,2,3,4]))