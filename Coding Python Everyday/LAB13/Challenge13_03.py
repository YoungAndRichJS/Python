# date 객체
from datetime import date

BIRTHDAY = {
    "Mom": (1969,11,5),
    "Dad": (1970,10,10),
    "Me": (2003,10,14)
}

def calculate():
    while True:
        name = input("Enter the name>> ").strip()
        year = date.today().strftime("%Y")
        if not name:
            break
        if name in BIRTHDAY:
            age = int(year) - BIRTHDAY[name][0] + 1
            print(f"{name}'s is {age} years old now.")
        else:
            print(f"Can't find {name}")
            
calculate()