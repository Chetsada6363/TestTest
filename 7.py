s = int(input())

h = s // 3600
m = (s % 3600) // 60
remains = s % 60

hstr = str(h).zfill(2)
mstr = str(m).zfill(2)
sstr = str(remains).zfill(2)

time_str = f"{hstr}:{mstr}:{sstr}"
print(time_str)