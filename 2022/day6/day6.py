import collections

def detect_distinct(n):
    buffer = collections.deque(maxlen=n)
    for i in range(0,len(data)):
        buffer.append(data[i])
        if len(set(buffer)) == n:
            return i+1
    return -1

def part_one():
    pos = detect_distinct(4)
    print(pos)

def part_two():
    pos = detect_distinct(14)
    print(pos)

if __name__ == "__main__":
    data = open("input").read()
    part_one()
    part_two()