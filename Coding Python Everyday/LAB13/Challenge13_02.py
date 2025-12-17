# 날씨 예보
WEATHER = {
    "1": 20,
    "2": 21,
    "3": 20,
    "4": 21,
    "5": 20,
    "6": 21,
}

def temperature():
    while True:
        date = input("Enter the date>> ").strip()
        if not date:
            break
        if date in WEATHER:
            temp = WEATHER[date]
            before = WEATHER.get(str(int(date)-1))
            after = WEATHER.get(str(int(date)+1))
        print(f"date{date} temperature will be {temp}C")
        print(f"day before the {date} temperature will be {before}C")
        print(f"day after the {date} temperature will be {after}C")

temperature()