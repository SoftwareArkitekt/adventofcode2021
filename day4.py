def formatInputv2(input):
    draws = input[0].split(",")
    games = []
    thisBoard = []
    for lineNumber in range(1, len(input)):
        record = input[lineNumber]
        if record == "stop":
            break
        if len(record) > 0:
            thisBoard = thisBoard + record.split()
        if len(thisBoard) == 25:
            games.append([thisBoard, 0])
            thisBoard = []
    return games, draws

#value & ~(1<<bit)
def part1(input):
    offset = 0
    winSum = 0
    games, draws = formatInputv2(input)
    for draw in draws:
        #print("Draw: %s" % draw)
        for game in games:
            #print("Game: ", game[0], format(game[1], 'b').zfill(25))
            if draw in game[0]:
                offset = int(game[0].index(draw))
                #print("Offset: %s" % offset)
                game[1] = game[1] | (16777216>>offset)
                #print(format(game[1],'b'))
                for check in (31, 992, 31744, 1015808, 32505856, 1082401, 2164802, 4329604, 8659208, 17318416): 
                    if game[1] & check == check:
                        print("Win!")
                        print("Hits: ",format(game[1],'b').zfill(25))
                        fhits = format(game[1] ^ 33554431, 'b').zfill(25)
                        print("invr: ", fhits)
                        for x in range(len(game[0])):
                            winSum += int(fhits[x]) * int(game[0][x])
                        return winSum * int(draw)

def part2(input):
    offset = 0
    winSum = 0
    games, draws = formatInputv2(input)
    for draw in draws:
        print(len(games))
        #print("Draw: %s" % draw)
        for game in games:
            #print("Game: ", game[0], format(game[1], 'b').zfill(25))
            if draw in game[0]:
                offset = int(game[0].index(draw))
                #print("Offset: %s" % offset)
                game[1] = game[1] | (16777216>>offset)
                #print(format(game[1],'b'))
                for check in (31, 992, 31744, 1015808, 32505856, 1082401, 2164802, 4329604, 8659208, 17318416): 
                    if game in games:
                        if game[1] & check == check and len(games) == 1:                        
                            print("Win!")
                            print("Draw: ", draw)
                            print("Board: ", games)
                            print("Chck: ", format(check, 'b').zfill(25))
                            print("Hits: ",format(game[1],'b').zfill(25))
                            fhits = format(game[1] ^ 33554431, 'b').zfill(25)
                            print("invr: ", fhits)
                            for x in range(len(game[0])):
                                winSum += int(fhits[x]) * int(game[0][x])
                            print((66 + 12 + 22 + 1 + 39) * 15)
                            return winSum * int(draw) 
                        elif game[1] & check == check and len(games) > 1:
                            games.remove(game)
                        # 2100 is too low
                        
if __name__ == '__main__':
    """
    t = 1
    s = 0
    for i in range(25):
        s += t
        print(i, t, s)
        t *= 2
    print(format(33554431,'b'))
    """
    i=list(open("4.txt").read().splitlines())
    print("Part 1")
    print(part1(i))
    print("Part 2")
    print(part2(i))
     # 37812 too low, 40572 to high