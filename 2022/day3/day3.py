def part_one(data):
    sum = 0
    priority = lambda a: ord(a) - ord('a') + 1 if a.islower() else ord(a) - ord('A') + 27
    for contents in data.splitlines():
        mid_index = len(contents)//2
        diff = list(set(contents[:mid_index]) & set(contents[mid_index:]))
        sum += priority(diff[0])
    print(sum)

if __name__ == "__main__":
    data = open("input").read()
    part_one(data)