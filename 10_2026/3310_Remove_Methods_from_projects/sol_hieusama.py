from typing import List


class Solution:

  def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
    bi_benh = [k]
    graph = {}

    for u, v in invocations:
      if u not in graph:
        graph[u] = []
      graph[u].append(v)

    quene = [k]
    while quene:
      u = quene.pop(0)

      for v in graph.get(u, []):
        if v not in bi_benh:
          bi_benh.append(v)
          quene.append(v)

    for u, v in invocations:
      if u not in bi_benh and v in bi_benh:
        return list(range(n))

    bi_benh_set = set(bi_benh)

    khong_benh = [i for i in range(n) if i not in bi_benh_set]

    return khong_benh