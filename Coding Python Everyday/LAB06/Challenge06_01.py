# 대문자화 우비두비 단어 만들기

def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                output.append(f"UB{letter}")
            else:
                output.append(f"ub{letter}")
        else:
            output.append(letter)
    return "".join(output)

print(ubbi_dubbi("Elephant"))
print(ubbi_dubbi("Soap"))
print(ubbi_dubbi("Octopus"))