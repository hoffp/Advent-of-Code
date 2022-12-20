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

def part_two():
    overlapping = [e for e in elf_list if e[0].overlaps(e[1])]
    print(len(overlapping))

def part_one():
    contains = [e for e in elf_list if e[0].contains(e[1]) or e[1].contains(e[0])]
    print(len(contains))

if __name__ == "__main__":
    data = open("input").read()
    for pair in data.splitlines():
        elves = pair.split(",")
        e1 = Elf(elves[0])
        e2 = Elf(elves[1])
        elf_list.append((e1,e2))
    part_one()
    part_two()