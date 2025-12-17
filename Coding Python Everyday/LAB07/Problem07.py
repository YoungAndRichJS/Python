# 문자열 정렬하기
def strsort(word): 
    output = sorted(word)
    return "".join(output)

print(strsort("cba"))
print(strsort("asdflkjhgzmxncbvpqowieuryt"))