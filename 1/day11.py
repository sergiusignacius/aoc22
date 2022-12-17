def main():
    with open("day1_input", "r") as f:
        data = f.readlines()

        calories_per_elf = []
        curr_calories = 0
        elf = 0

        for l in data:
            line = l.strip()
            if len(line) == 0:
                calories_per_elf.append((curr_calories, elf))
                elf += 1
                curr_calories = 0
            else:
                curr_calories += int(line)
        
        print(sum(item[0] for item in sorted(calories_per_elf, reverse=True, key=lambda x: x[0])[0:3]))


main()