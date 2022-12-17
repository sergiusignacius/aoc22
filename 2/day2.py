# ROCK      AX
# PAPER     BY
# SCISSORS  CZ

play_scores = { 'X': 1, 'Y': 2, 'Z': 3 }

def normalize(play):
    return chr(ord('A') + ord(play) - ord('X'))

def parse(path):
    with open(path) as f:
        return [line.strip().split(" ") for line in f]

def fight(a, b):
    if a == b: return 3
    else:
        return 6 if (a == 'A' and b == 'B') or (a == 'B' and b == 'C') or (a == 'C' and b == 'A') else 0

def score(play):
    return play_scores[play[1]] + fight(play[0], normalize(play[1]))

def solve(input):
    return sum([score(play) for play in input])

assert normalize('Z') == 'C'
print(solve(parse("day2_test")))
assert solve(parse("day2_test")) == 15
print(solve(parse("day2_input")))


normalized = { 'A': 1, 'B': 2, 'C': 3 }

def clamp(x, inc):
    return (x + 2 + (inc % 3)) % 3 + 1

assert clamp(1, 1) == 2
assert clamp(2, 1) == 3
assert clamp(3, 1) == 1
assert clamp(1, -1) == 3
assert clamp(2, -1) == 1
assert clamp(3, -1) == 2

def shape(play):
    theirs, outcome = play
    if outcome == 'X':
        return chr(ord('X') + clamp(normalized[theirs], -1) - 1)
    elif outcome == 'Y':
        return chr(ord('X') + ord(theirs) - ord('A'))
    else:
        return chr(ord('X') + clamp(normalized[theirs], 1) - 1)

assert shape(('A', 'X')) == 'Z'
assert shape(('A', 'Y')) == 'X'
assert shape(('A', 'Z')) == 'Y'

assert shape(('B', 'X')) == 'X'
assert shape(('B', 'Y')) == 'Y'
assert shape(('B', 'Z')) == 'Z'

assert shape(('C', 'X')) == 'Y'
assert shape(('C', 'Y')) == 'Z'
assert shape(('C', 'Z')) == 'X'

def solve2(input):
    return solve([(play[0], shape(play)) for play in input])

assert solve2(parse("day2_test")) == 12
print(solve2(parse("day2_input")))