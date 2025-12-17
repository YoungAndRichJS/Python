# 비밀언어 우비두비 만들기

def ubbi_dubbi(*word):
    output = []
    for char in word:
        if char in "aeiou":
            char = f"ub{char}"
            output.append(char)
        else:
            output.append(char)
    return "".join(output) 

# print results
print(ubbi_dubbi("elephant"))
print(ubbi_dubbi("soap"))
print(ubbi_dubbi("octopus"))