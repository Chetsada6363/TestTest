input_num = []
for i in range(10):
    num = int(input(f"ตัวที่ {i+1}: "))
    input_num.append(num)

for i in range(len(input_num)):
    for j in range(0, len(input_num) - i - 1):
        if input_num[j] < input_num[j + 1]:
            input_num[j], input_num[j + 1] = input_num[j + 1], input_num[j]

print(input_num)
