class Solution(object):
    cir = 0
    
    def walkThrough(self, nodes, current, stack):
        if self.cir == 1:
            return
        stack.append(current)

        if current in nodes:
            sons = list(nodes[current])
            for son in sons:
                if son in stack:
                    self.cir = 1
                    return
                else:
                    self.walkThrough(nodes, son, stack)
        stack.pop()
        nodes[current] = set()
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nodes = dict()
        sonSet = set()
        roots = list()
        for one in prerequisites:
            if one[0] == one[1]:
                return False
            if one[0] in nodes:
                nodes[one[0]].add(one[1])
            else:
                nodes[one[0]] = set([one[1]])
            sonSet.add(one[1])

        if len(nodes.keys()) > numCourses:
            return False
        for one in nodes.keys():
            if not one in sonSet:
                roots.append(one)
        if len(roots) == 0:
            return False
        stack = []
        for one in roots:
            self.walkThrough(nodes, one, stack)
        if self.cir == 1:
            return False

        return True

S = Solution()
print S.canFinish(3,[[0,1],[0,2],[1,2]])
print S.canFinish(4,[[0,1],[3,1],[1,3],[3,2]])
#print S.canFinish(1,[])
