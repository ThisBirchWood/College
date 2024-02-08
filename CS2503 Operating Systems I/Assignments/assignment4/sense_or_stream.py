infile = open("sense_or_steam.txt", "r")
lines = [int(line.strip()) for line in infile.readlines()]
infile.close()

trend_alert = 'N'
trends = []

for i in range(len(lines)):
    previous = lines[i-1]
    previous2 = lines[i-2]
    current = lines[i]
    if i >= 2:
        if current > previous and previous > previous2:
            trends.append('U')
        elif current < previous and previous < previous2:
            trends.append('D')
        else:
            trends.append('N')
    else:
        trends.append('N')

    if lines[i] >= lines[i-1]:
        if trends[i-1] == "D":
            trends[i] = 'E'
    if lines[i] <= lines[i-1]:
        if trends[i-1] == "U":
            trends[i] = 'E'

    if trends[i-1] == "E":
        if trends[i] == "U":
            trends[i] = 'RU'
        elif trends[i] == "D":
            trends[i] = 'RD'

for i in range(len(lines)):
    print(lines[i], trends[i])