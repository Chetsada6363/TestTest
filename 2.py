def c(s1, s2):
    s1_lower = ""
    s2_lower = ""

    for char in s1:
        s1_lower += char.lower()
    for char in s2:
        s2_lower += char.lower()

    if len(s1) != len(s2):
        return False
    
    ss1 = []
    ss2 = []

    for char in s1_lower:
        ss1.append(char)
    for char in s2_lower:
        ss2.append(char)

    ss1.sort()
    ss2.sort()

    if ss1 == ss2:
        return True
    else:
        return False

input_s1 = input("s1:")
input_s2 = input("s2:")

result = c(input_s1, input_s2)
print(result)
