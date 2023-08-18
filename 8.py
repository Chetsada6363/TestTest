num = int(input())

money = 1000 - num
a = []

m500 = money // 500
if m500 == 1:
    a.append(f"500 {m500} ใบ")

m100 = (money % 500) // 100
if m100 > 0:
    a.append(f"100 {m100} ใบ")

m50 = (money % 100) // 50
if m50 > 0:
    a.append(f"50 {m50} ใบ")

m10 = (money % 50) // 10
if m10 > 0:
    a.append(f"10 {m10} เหรียญ")

m1 = money % 10
if m1 > 0:
    a.append(f"1 {m1} เหรียญ")

print("จำนวนเงินทอน", money, "บาท")
for item in a:
    print(item)
