class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = {}
        for u, v in invocations:
            if u not in graph:
                graph[u]=[]
            graph[u].append(v)
        nghi_ngo={k}
        stack=[k]
        while stack:
            current=stack.pop()
            if current in graph:
                for i in graph[current]:
                    if i not in nghi_ngo:
                        nghi_ngo.add(i)
                        stack.append(i)
        for u, v in invocations:
            if u not in nghi_ngo and v in nghi_ngo:
                return list(range(n))
        result=[]
        for i in range(n):
            if i not in nghi_ngo:
                result.append(i)
        return result

