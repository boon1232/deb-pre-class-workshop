temperatures =  [35, 25, 26, 25, 29, 27, 38]

total = sum(temperatures)
average = total/len(temperatures)

print("Part 1 :")
print(f"1. เฉลี่ยยอดขาย: {average}")
print(f"1. เฉลี่ยยอดขาย: {average:.2f}")

print("Part 2 :")
for i, s in enumerate(temperatures):
    print(f"วันที่ {i + 1} มีค่า {s} องศา")

print("Part 3 :")

def classify(t, avg):
    # return "ร้อน" if t > avg else "เย็น"
    if t > avg:
        return "ร้อน"
    elif t <= avg:
        return "เย็น"
    else: "ไม่รู้"

print(classify(29.286, average))

import pandas as pd


df = pd.read_csv("pokemon.csv")
print(df.head())