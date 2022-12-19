def part_one(data):
    sum = 0
    calories = []
    for i in data.splitlines():
        if i.isnumeric():
            sum += eval(i)
        else:
            calories.append(sum)
            sum = 0
    return calories

def part_two(calories):
    print(sum(sorted(calories, reverse=True)[:3]))    
    

if __name__ == "__main__":
    data = open("input").read()
    calories = part_one(data)
    part_two(calories)