class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        prereqMap = defaultdict(list)
        for e in prerequisites:
            prereqMap[e[0]].append(e[1])

        totalVisited = set()
        localVisited = set()

        def dfs(course):
            # print(localVisited)
            nonlocal localVisited
            if course in localVisited:
                return False
            if course in totalVisited:
                return True

            localVisited.add(course)
            totalVisited.add(course)

            valid = True
            if course in prereqMap:
                for e in prereqMap[course]:
                    temp = localVisited.copy()
                    valid = valid and dfs(e)
                    localVisited = temp
            return valid


        res = True
        for e in prereqMap:
            res = res and dfs(e)
            localVisited = set()
        return res