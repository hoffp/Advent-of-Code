def part_one(data):
    calories = map(sum, [map(int, i.split("\n")) for i in data.split("\n\n")])
    return list(calories)

def part_two(calories):
    print(sum(sorted(calories, reverse=True)[:3]))    
    
if __name__ == "__main__":
    data = open("input").read()
    data = part_one(data)
    print(max(data))
    part_two(data)