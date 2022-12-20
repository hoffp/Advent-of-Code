class Elf:
    min = 0
    max = 0
    sect_cover = []

    def __init__(self, sections) -> None:

        self.min = int(sections.split("-")[0])
        self.max = int(sections.split("-")[1])
        self.sect_cover = range(self.min, self.max + 1)

    def contains(self, elf):
        return elf.min <= self.min and self.max <= elf.max

    def overlaps(self, elf):
        return not set(self.sect_cover).isdisjoint(set(elf.sect_cover))

elf_list = []

def part_two(data):
    count = 0
    for pair in elf_list:
        if pair[0].overlaps(pair[1]):
            count += 1
    print(count)


def part_one(data):
    count = 0
    for pair in data.splitlines():
        elves = pair.split(",")
        e1 = Elf(elves[0])
        e2 = Elf(elves[1])
        elf_list.append((e1,e2))
        if e1.contains(e2) or e2.contains(e1):
            count += 1

    print(count)

if __name__ == "__main__":
    data = open("input").read()
    part_one(data)
    part_two(data)