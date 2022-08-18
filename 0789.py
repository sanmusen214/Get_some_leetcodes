class Solution:
    def escapeGhosts(self, ghosts: "List[List[int]]", target: "List[int]") -> bool:
        def distance(start,end):
            return abs(end[0]-start[0])+abs(end[1]-start[1])
        player_dis=distance([0,0],target)
        for i in ghosts:
            if(distance(i,target)<=player_dis):
                return False
        return True