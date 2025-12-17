# 모음 많이 들어간 단어 찾기

def most_repeating_vowels(words):
    return max(words, key= most_repeating_vowels_count) 

def most_repeating_vowels_count(word):
    count = sum(1 for letter in word if letter in "aeiou")
    return count

print(most_repeating_vowels(["this", "is", "an", "elementary",\
                            "test", "example" ]))