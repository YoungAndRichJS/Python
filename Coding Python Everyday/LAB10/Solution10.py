# 이름을 알파벳 순서로 정렬하기
import operator

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
    for p in sorted(people, key= operator.itemgetter("last", "first")):
        print(f"{p["last"]}, {p["first"]}: {p["email"]}")
    
alphabetiz_names(PEOPLE)