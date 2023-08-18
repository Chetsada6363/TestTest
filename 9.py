str = input()
words = str.split()
rewords = []

for word in words:
    r = ""
    for char in word:
        r = char + r
    rewords.append(r)

restr = " ".join(rewords)
print(restr)
