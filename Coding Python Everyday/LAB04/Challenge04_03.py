# 모음 2개 이상 피그 라틴어

def pig_lattin(word):
    vowel = "aeiou"
    is_more_than_2_vowel = False
    word_index = 0
    for char in word:
        if char in vowel:
            for char2 in word[word_index+1:]:
                if char2 in vowel:
                    is_more_than_2_vowel = True
                    break
        word_index +=1
    
    if is_more_than_2_vowel:
        return f"{word[:-1]}way" + word[-1]
    else:
        return f"{word[1:-1]}" + word[0] + "ay" + word[-1]


print(pig_lattin("english!"))
print(pig_lattin("python@"))
print(pig_lattin("wine;"))
print(pig_lattin("wind%"))