priority = lambda a: ord(a) - ord('a') + 1 if a.islower() else ord(a) - ord('A') + 27

def part_one(data):
    sum = 0
    for contents in data.splitlines():
        mid_index = len(contents)//2
        diff = set(contents[:mid_index]) & set(contents[mid_index:])
        sum += priority(list(diff)[0])
    print(sum)

def part_two(data):
    sum = 0
    groups = [data.splitlines()[i:i + 3] for i in range(0, len(data.splitlines()), 3)]
    for group in groups:
        badge = set(group[0]) & set(group[1]) & set(group[2])
        sum += priority(list(badge)[0])
    print(sum)

if __name__ == "__main__":
    data = open("input").read()
    part_one(data)
    part_two(data)