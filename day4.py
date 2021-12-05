#value & ~(1<<bit)
def part1v2(input):
    draws = input[0].split(",")
    boards = [] # Master list of bingo boards
    hits = []
    i = 0
    for lineNumber in range(1, len(input)):
        record = input[lineNumber]
        # Check for whitespace
        if len(record) == 0:
            boards.append([])
            hits.append(0)
            i = len(boards) - 1
        else:
            boards[i] = boards[i] + record.split()
    #print(boards)
    
    for draw in draws:
        for board in boards:
            if draw in board:
                hits[boards.index(board)] = hits[boards.index(board)] | (1<<board.index(draw))
                for check in (31, 992, 31744, 1015808, 32505856, 1082401, 2164802, 4329604, 8659208, 17318416): 
                    #print(format(check,'b').zfill(25))
                    if hits[boards.index(board)] & check == check:
                        boardSum = 0
                        paddedHits = format(hits[boards.index(board)],'b').zfill(25)
                        invertedHits = [int(x)^1 for x in paddedHits]
                        print("Inverted Hits: %s" % invertedHits)
                        for token, remainder in zip(board, invertedHits):
                            boardSum += int(token) * int(remainder)
                            print("%s * %s + %s = %s" % (token, remainder, boardSum, int(token)*int(remainder)+boardSum))
                        print(boardSum)
                  
                        
                            
                        print("Draw: %s Winstate: %s" % (draw, paddedHits))
                        return int(draw) * int(boardSum)
                        # 37812 too low, 40572 to high
    
if __name__ == '__main__':
    i=list(open("4.txt").read().splitlines())
    print("Part 1")
    print(part1v2(i))