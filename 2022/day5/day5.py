class Stack:
    crates = []

    def __init__(self) -> None:
        self.crates = []

    def __str__(self) -> str:
        return str(["["+str(c)+"]" for c in self.crates])

    def add_crate(self, c):
        self.crates.append(c)

class Crate:
    contents = ''

    def __init__(self, c) -> None:
        self.contents = c

    def __str__(self) -> str:
        return self.contents

    def move(self, old, new):
        old.remove_crate(self)
        new.add_crate(self)

stacks = [Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack()]

def part_one(data):
    start_config = data.split("\n\n")[0]

    for row in start_config.splitlines():
        stack_index = 0
        for n in range(1, len(row), 4):
            if row[n].isalpha():
                stacks[stack_index].add_crate(Crate(row[n]))
            stack_index += 1
    
    move_set = data.split("\n\n")[1]
    
if __name__ == "__main__":
    data = open("input").read()
    part_one(data)