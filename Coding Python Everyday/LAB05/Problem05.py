# 피그 라틴 문장 만들기

def pl_sentence(sentence):
    words = sentence.split(" ")
    result = []
    for word in words:
        if word[0] in "aeiou":
            result.append(f"{word}way")
        else:
            result.append(word[1:] + word[0] + "ay")
            
    for word in result:
        print(word, end=" ")


pl_sentence("this is a test translation")