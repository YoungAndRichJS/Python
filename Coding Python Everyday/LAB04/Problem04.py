# 피그 라틴 단어 만들기

def pig_lattin(word):
    if word[0] in "aeiou":
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"

print(pig_lattin("python")) 
