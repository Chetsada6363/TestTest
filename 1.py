def p(array, tsum):
    pp = []

    for i, num1 in enumerate(array):
        for j, num2 in enumerate(array[i + 1:], start=i + 1):
            if num1 + num2 == tsum:
                pp.append((num1, num2))

    return pp

input_str = input()
array = list(map(int, input_str.split()))

tsum = int(input())

result = p(array, tsum)

if result:
    for pp in result:
        print(pp[0], ",", pp[1])
else:
    print("non", tsum)

