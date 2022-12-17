def parse(input):
    with open(input, "r") as f:
        return [[[int(a) for a in assignment.split("-")] for assignment in line.strip().split(",")] for line in f]

def contains(a, b):
    c1 = (a[0] >= b[0] and a[0] <= b[1] and a[1] >= b[0] and a[1] <= b[1])
    c2 = (b[0] >= a[0] and b[0] <= a[1] and b[1] >= a[0] and b[1] <= a[1])
    return c1 or c2

def solve(input):
    return len([pair for pair in input if contains(pair[0], pair[1])])

print(parse("day4_test"))
print(solve(parse("day4_test")))

print(solve(parse("day4_input")))

def contains2(a, b):
    c1 = (a[0] >= b[0] and a[0] <= b[1] or a[1] >= b[0] and a[1] <= b[1])
    c2 = (b[0] >= a[0] and b[0] <= a[1] or b[1] >= a[0] and b[1] <= a[1])
    return c1 or c2

def solve2(input):
    return len([pair for pair in input if contains2(pair[0], pair[1])])

print(solve2(parse("day4_test")))

print(solve2(parse("day4_input")))