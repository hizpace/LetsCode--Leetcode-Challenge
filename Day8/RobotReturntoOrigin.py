class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u_count = 0
        d_count = 0
        l_count = 0
        r_count = 0
        for move in moves:
            match move:
                case "U": 
                    u_count+=1
                case "D": 
                    d_count+=1
                case "L":
                    l_count+=1
                case "R":
                    r_count+=1
                case _:
                    pass
        if u_count==d_count and l_count==r_count:
            return True
        else:
            return False


        
