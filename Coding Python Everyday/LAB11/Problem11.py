# 특정 글자를 가장 많이 가진 단어 찾기
import operator

def most_repeating_word(words):
    output = words[0]
    max_count = search_and_count_the_alphabet(words[0])

    for word in words[1:]:
        count = search_and_count_the_alphabet(word)
        if count > max_count:
            max_count = count
            output = word
    return output

def search_and_count_the_alphabet(word):
    set_of_alphabet = []
    for alphabet in word:
        count = sum(1 for char in word if char == alphabet)
        set_of_alphabet.append({"alphabet":alphabet, "count":count})
    output = max(set_of_alphabet,key= operator.itemgetter("count"))["count"]
    return output


# ababbcccc
print(most_repeating_word(["this", "is", "an", "elementary",\
                            "test", "example" ]))