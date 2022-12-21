class Stack:
    crates = []

    def __init__(self) -> None:
        self.crates = []

    def __str__(self) -> str:
        return str(["["+str(c)+"]" for c in self.crates])

    def add_crate(self, c):
        self.crates.insert(0,c)

    def move_crate(self, s):
        s.add_crate(self.crates.pop(0))

stacks = [Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack()]

def part_one(data):
    data = data.split("\n\n")

    start_config = data[0].splitlines()
    for row in reversed(start_config):
        stack_index = 0
        for n in range(1, len(row), 4):
            if row[n].isalpha():
                stacks[stack_index].add_crate(row[n])
            stack_index += 1
    
    move_set = data[1].splitlines()
    for move in move_set:
        move = move.split(" ")

        number_of_crates = int(move[1])
        from_stack = stacks[int(move[3]) - 1]
        to_stack = stacks[int(move[5]) - 1]

        for n in range(0, number_of_crates):
            from_stack.move_crate(to_stack)
        
    print(''.join([s.crates[0] for s in stacks]))
    
if __name__ == "__main__":
    data = open("input").read()
    part_one(data)