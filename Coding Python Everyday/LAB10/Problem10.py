# 이름을 알파벳 순서로 정렬하기
PEOPLE = {
    "first": "Reuven", "last": "Lerner",
    "email": "reuven@lerner.co.il"
},{
    "first": "Donald", "last": "Trump",
    "email": "president@whitehouse.gov"
},{
    "first": "Vladimir", "last": "Putin",
    "email": "president@kremvax.ru"
}

def alphabetiz_names(people):
    return sorted(people, key= lambda x: [x["last"], x["first"]])

print(alphabetiz_names(PEOPLE))