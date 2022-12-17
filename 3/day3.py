def parse(input):
    result = []
    with open(input, "r") as f:
        for line in f:
            half = len(line) >> 1
            result.append((line[:half], line[half:]))
    return result

def priority(el):
    return ord(el) + (1 - ord('a') if el >= 'a' and el <= 'z' else 27 - ord('A'))

def intersect(a, b):
    return set(a).intersection(set(b)).pop()

def solve(input):
    return sum([priority(intersect(h0, h1)) for h0,h1 in input])

assert solve(parse("day3_test")) == 157
print(solve(parse("day3_input")))

def parse2(input):
    with open(input, "r") as f:
        return [line.strip() for line in f]

def intersect3(a, b, c):
    return set(a).intersection(set(b)).intersection(set(c)).pop()

def solve2(input):
    return sum([priority(intersect3(*tuple)) for tuple in zip(*[iter(input)] * 3)])

assert solve2(parse2("day3_test")) == 70
print(solve2(parse2("day3_input")))