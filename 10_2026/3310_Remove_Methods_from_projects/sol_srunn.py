from collections import deque
class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for u,v in invocations:
            graph[u].append(v)
        my_set = set()
        queue = deque([k])
        my_set.add(k)
        while queue:
            curr = queue.popleft()
            for i in graph[curr]:
                if i not in my_set:
                    my_set.add(i)
                    queue.append(i)
        co_the_xoa=False
        for u,v in invocations:
            if v in my_set and u not in my_set:
                co_the_xoa=True
                break
        if co_the_xoa:
            return [i for i in range(n)]
        return [ i for i in range(n) if i not in my_set]

