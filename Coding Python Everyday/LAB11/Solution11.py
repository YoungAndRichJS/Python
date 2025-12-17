# 특정 글자를 가장 많이 가진 단어 찾기
from collections import Counter
import operator

def most_repeating_word(words):
    output = max(words, key= most_repeating_letter_count)
    return output
        
def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1] 
    
print(most_repeating_word(["this", "is", "an", "elementary",\
                            "test", "example" ]))