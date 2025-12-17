# 구두점 처리

def pig_lattin(word):
    if word[0] in "aeiou":
        return f"{word[:-1]}way" + word[-1]
    else:
        return f"{word[1:-1]}" + word[0] + "ay" + word[-1]

print(pig_lattin("english?"))
print(pig_lattin("computer!"))