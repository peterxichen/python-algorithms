# Alien Dictionary (lexicographical, topological sort)
# topological sort:  linear ordering of vertices such that for every directed edge u->v, 
# u comes before v in the ordering (possible iff is DAG, no directed cycles)
# create dicts adjacents + num indegrees for each unique letter
# BFS -> repeatedly "pick off" nodes w/ indegree 0
# time: O(total length of all the words in the input list), space: O(1 e.g. num unique chars in alphabet)
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # get dependency rules into graph then topological sort
        # node=letters, edge-dependencies (e.g. A before B)
        
        # create adjacents + num indegress for each unique letter
        adjacents = {c: [] for w in words for c in w}
        indegrees = {c: 0 for w in words for c in w}
        for w1, w2 in zip(words, words[1:]): # for each pair of adjacent words
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adjacents[c1]:
                        adjacents[c1].append(c2)
                        indegrees[c2] += 1
                    break
            # else executes at the end if break not executed
            else: # no solution: w2 is a prefix of w1
                if len(w2) < len(w1):
                    return ""
        
        # BFS: repeatedly "pick off" nodes w/ indegree 0
        ret = []
        queue = [c for c in indegrees if indegrees[c]==0]
        while queue:
            c = queue.pop(0)
            ret.append(c)
            # traverse adjacent nodes
            for n in adjacents[c]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)
        # not all letters are in ret -> cycle/no solution
        if len(ret) < len(indegrees):
            return ""
        return "".join(ret)
