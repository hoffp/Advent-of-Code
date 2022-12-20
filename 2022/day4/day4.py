class Elf:
    start = 0
    end = 0

    def __init__(self, s, e) -> None:
        self.start = s
        self.end = e

def part_one(data):
    elves = [Elf(y[0].split("-")[0], y[1].split("-")[1]) for y in [x.split(",") for x in data.splitlines()]]
    print(elves)
    # for sections in data:
    #     for elf in sections:
    #         elf = elf.split("-")
    #         print(elf[0] + " and " + elf[1])
    #         e = Elf(elf[0], elf[1])
    #         elves.append(e)
        

    #print(data)

if __name__ == "__main__":
    data = open("input").read()
    part_one(data)