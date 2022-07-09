# Course Schedule
# topological sort: linear ordering of vertices such that for every directed edge u->v, 
# u comes before v in the ordering (possible iff is DAG, no directed cycles)
# data structure tracks num of inbounds + out nodes, create graph of courses
# BFS -> remove outgoing edges w/ 0 inbounds (no dependencies) 1 by 1
# return True if no cycle (no edges remaining after top. sort)
# time: O(E+V), space: O(E+V)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # data structure for graph node
        class GNode():
            def __init__(self):
                self.inNodeNum = 0
                self.outNodes = []

        graph = {} # create graph of courses
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            if graph.get(prevCourse) is None:
                graph[prevCourse] = GNode()
            if graph.get(nextCourse) is None:
                graph[nextCourse] = GNode()
                
            # append to outNodes and add inNode
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inNodeNum += 1
        
        noDepCourses = [] # queue of courses w/ no incoming edge
        for k,v in graph.items():
            if v.inNodeNum == 0:
                noDepCourses.append(k)
        
        # only needed if want to return sorted courses
        #sortedCourses = [] # "removed" nodes
        
        # BFS: remove outgoing edges 1 by 1
        while noDepCourses:
            course = noDepCourses.pop(0)
            # sortedCourses.append(course)
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inNodeNum -= 1
                if graph[nextCourse].inNodeNum == 0:
                    noDepCourses.append(nextCourse)
            graph[course].outNodes = [] # empty outnodes
            
        # check for cycle (if edge still remains)
        for k,v in graph.items():
            if len(v.outNodes) > 0:
                return False
        return True
