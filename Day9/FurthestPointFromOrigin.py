class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count("L")
        r = moves.count("R")
        if l>r:
            moves = moves.replace("_","L")
        elif r>l:
            moves = moves.replace("_","R")
        else:
            if moves.startswith("L"):
               moves = moves.replace("_","L")
            elif moves.startswith("R"):
                moves = moves.replace("_","R")
            else:
                moves = moves.replace("_","R")    
        c = 0
        for i in moves:
            if i=="L":
                c -= 1
            elif i=="R":
                c += 1
        
        return abs(c)
