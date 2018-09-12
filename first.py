with open('data.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            polyShape.append(line)
            print(polyShape)