def main():
    with open("day1_input", "r") as f:
        data = f.readlines()

        max_calories = 0
        curr_calories = 0
        for l in data:
            line = l.strip()
            if len(line) == 0:
                curr_calories = 0
            else:
                curr_calories += int(line)
                if curr_calories > max_calories:
                    max_calories = curr_calories
                
        print(max_calories)

main()