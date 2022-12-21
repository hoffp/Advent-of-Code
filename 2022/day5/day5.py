import copy

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
    
    def move_stack(self,s,n):
        for i in range(n-1,-1,-1):
            s.add_crate(self.crates.pop(i))

def part_one(stacks):
    for move in move_set:
        move = move.split(" ")

        number_of_crates = int(move[1])
        from_stack = stacks[int(move[3]) - 1]
        to_stack = stacks[int(move[5]) - 1]

        for n in range(0, number_of_crates):
            from_stack.move_crate(to_stack)
        
    print(''.join([s.crates[0] for s in stacks]))

def part_two(stacks):
    for move in move_set:
        move = move.split(" ")

        number_of_crates = int(move[1])
        from_stack = stacks[int(move[3]) - 1]
        to_stack = stacks[int(move[5]) - 1]

        from_stack.move_stack(to_stack, number_of_crates)
    
    print(''.join([s.crates[0] for s in stacks]))

    
if __name__ == "__main__":
    data = open("input").read().split("\n\n")
    start_config = data[0].splitlines()
    move_set = data[1].splitlines()
    initial_stack = [Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack()]
    
    for row in reversed(start_config):
        stack_index = 0
        for n in range(1, len(row), 4):
            if row[n].isalpha():
                initial_stack[stack_index].add_crate(row[n])
            stack_index += 1

    part_one(copy.deepcopy(initial_stack))
    part_two(copy.deepcopy(initial_stack))