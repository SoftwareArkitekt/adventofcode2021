f=list(open("2.txt").read().splitlines())
depth = 0
distance = 0

for line in f:
    i = line.split()
    if i[0] == "forward":
        distance += int(i[1])
    elif i[0] == "down":
        depth += int(i[1])
    else: 
        depth -= int(i[1])

print(depth)
print(distance)
print(depth*distance)

depth = 0
distance = 0
aim = 0
for line in f:
    i = line.split()
    if i[0] == "forward":
        distance += int(i[1])
        depth += int(i[1]) * aim
    elif i[0] == "down":
        aim += int(i[1])
    else: 
        aim -= int(i[1])

print(distance)
print(depth)
print(distance*depth)