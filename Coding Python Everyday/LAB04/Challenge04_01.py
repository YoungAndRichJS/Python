# 대문자 피그 라틴어

def pig_lattin(word):
    vowel = "aeiou"

    if word[0].lower() in vowel:
        return f"{word}way"
    else:
        word = word[1].upper() + word[2:] + word[0].lower() + "ay"
        return word

print(pig_lattin("English"))
print(pig_lattin("computer"))