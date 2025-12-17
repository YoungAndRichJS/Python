# 문자열 모음 수로 정렬하기
def vowel(*words):
    output = sorted([word for word in words], key=how_many_vowels)
    return ", ".join(output)

def how_many_vowels(word):
    # vowels_number = 0
    # for alphabet in word:
    #     if alphabet.lower() in "aeiou":
    #         vowles_number += 1
    # return vowels_number
    return sum(1 for ch in word.lower() if ch in "aeiou")

print(vowel("aeiou", "aeio", "AEI", "AE", "a"))