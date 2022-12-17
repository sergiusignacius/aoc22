import re
command_regex = re.compile(r'^\$ (\w+)\s?(.*)?$')
result_regex = re.compile(r'^(\d+|dir)\s(.+)')

def parse(input):
    with open(input, "r") as f:
        lines = f.readlines()
        i = 0
        commands = []
        while i < len(lines):
            command_match = command_regex.match(lines[i])

            i += 1
            if command_match:
                command = command_match[1]
                if command == "cd":
                    commands.append({"command": command, "result": command_match[2]})
                else:
                    contents = []
                    commands.append({"command": command, "result": contents})
                    while i < len(lines) and (res := result_regex.match(lines[i])) is not None:
                        if res[1] == "dir":
                            contents.append({"type": "dir", "name": res[2]})
                        else:
                            contents.append({"type": "file", "name": res[2], "size": int(res[1])})
                        i += 1
        return commands

def build_tree(input):
    root = {'children': {}, 'size': None }
    cwd = root
    stack = ["/"]

    for c in input:
        if c["command"] == "cd":
            if c["result"] == "..":
                stack.pop()
                cwd = stack[-1]
            elif c["result"] == "/":
                cwd = root
                stack = [cwd]
            else:
                cwd = cwd['children'][c["result"]]
                stack.append(cwd)
        elif c["command"] == "ls":
            for r in c["result"]:
                if r["type"] == "dir":
                    cwd['children'][r["name"]] = {'children': {}, 'size': None }
                else:
                    cwd['children'][r["name"]] = { 'size': r["size"] }

    return root

def update_sizes(root):
    if root['size'] is None:
        root['size'] = sum(update_sizes(c) for c in root['children'].values())

    return root['size']

def directories(root):
    if 'children' in root:
        for c in root['children'].values():
            if 'children' in c:
                yield c
                yield from directories(c)

root = build_tree(parse("day7_input"))
update_sizes(root)

sum_sizes = sum([d['size'] for d in directories(root) if d['size'] <= 100000])

print(sum_sizes)

total_space = 70000000
used_space = root['size']
free_space = total_space - used_space
to_delete = 30000000 - free_space

print(used_space, free_space, to_delete)

candidates = sorted([d['size'] for d in directories(root) if d['size'] >= to_delete])

print(candidates)