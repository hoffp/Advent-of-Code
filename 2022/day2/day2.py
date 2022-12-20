score_table = { 'A X':4, 'A Y':8, 'A Z':3
              , 'B X':1, 'B Y':5, 'B Z':9
              , 'C X':7, 'C Y':2, 'C Z':6
              }

def part_one(data):  
    score = sum([score_table[x] for x in data.splitlines()])
    print(score)

def part_two(data):
    x = [x.split() for x in data.splitlines()]
    print(x)

if __name__ == "__main__":
    data = open("input").read()
    #part_one(data)
    part_two(data)