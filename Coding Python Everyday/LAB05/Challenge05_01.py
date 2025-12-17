# 텍스트 파일을 읽어들이고 추출해서 문장만들기
with open("test.txt", "w") as file:
    while True:
        str = input("Enter the sentence> ")
        if not str:
            break
        file.write(str+"\n")

with open("test.txt","r") as file:
    n = int(input("Enter the number u want> "))
    output = []
    for line in file:
        str = list(line.split(" "))
        output.append(str[n-1])
    
    print(" ".join(output))