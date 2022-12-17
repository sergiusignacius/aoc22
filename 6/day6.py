def solve(input, length=3):
    with open(input, "r") as f:
        input = f.read().strip()
        trailing = 0
        for i in range(len(input)):
            if i < length:
                continue
            else:
                substr = input[trailing:i+1]
                if len(substr) == len(set(substr)):
                    return i + 1
                else:
                    trailing += 1

assert solve("day6_test") == 7
print(solve("day6_input"))

assert solve("day6_test", length=13) == 19
print(solve("day6_input", length=13))