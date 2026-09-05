class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        res = []

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                if course not in res:
                    res.append(course)
                return True

            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            preMap[course] = []
            if course not in res:
                res.append(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return []
        return res