def parse(input):
    with open(input, "r") as f:
        map = []
        for line in f:
            line = line.strip()
            row = []
            for c in line:
                row.append(int(c))
            map.append(row)
        
        return map
    
def is_visible(row, col, map):
    height = map[row][col]
    left = map[row][0:col]
    right = map[row][col+1:len(map[row])]
    top = [map[r][col] for r in range(0, row)]
    bottom = [map[r][col] for r in range(row+1, len(map))]

    return any(all([t < height for t in trees]) for trees in [left, right, top, bottom])

def solve(input):
    visible_count = 2 * len(input) + 2 * len(input[0]) - 4
    for i in range(1, len(input) - 1):
        for j in range(1, len(input[0]) - 1):
            if is_visible(i, j, input):
                visible_count += 1
    
    return visible_count

print(solve((parse("day8_input"))))
# assert solve((parse("day8_test"))) == 21