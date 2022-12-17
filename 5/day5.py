import re

crate_regex = re.compile(r'^\s*\[')
move_regex = re.compile(r'^move (\d+) from (\d+) to (\d+)$')

def parse(input):
    with open(input, "r") as f:
        lines = f.readlines()
        crate_rows = []
        moves = []
        for line in lines:
            crate_match = crate_regex.match(line)
            move_match = move_regex.match(line)
            if crate_match:
                row = []
                for i in range(0, len(line), 4):
                    row.append(None if line[i] == ' ' else line[i+1])

                crate_rows.append(row)
            elif move_match:
                moves.append((int(move_match[1]), int(move_match[2]) - 1, int(move_match[3]) - 1))

        stacks = [[c[i] for c in reversed(crate_rows) if c[i] is not None] for i in range(len(crate_rows[0]))]
        
        return stacks, moves
    
def solve(input):
    stacks, moves = input
    for move in moves:
        for i in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())

    return ''.join([s[-1] for s in stacks])

assert solve(parse("day5_test")) == 'CMZ'
print(solve(parse("day5_input")))

def solve2(input):
    stacks, moves = input
    for move in moves:
        stacks[move[2]].extend(stacks[move[1]][-move[0]:])
        stacks[move[1]] = stacks[move[1]][:-move[0]]
        
    return ''.join([s[-1] for s in stacks])

assert solve2(parse("day5_test")) == 'MCD'
print(solve2(parse("day5_input")))