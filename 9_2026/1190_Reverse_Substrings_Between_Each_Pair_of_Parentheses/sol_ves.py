class Solution:
  def reverseParentheses(self, s: str) -> str:
    n = len(s)
    pair = [0] * n
    stack = []
    for i, char in enumerate(s):
      if char == "(":
        stack.append(i)
      elif char == ")":
        j = stack.pop()
        pair[i] = j
        pair[j] = i
    res = []
    curr = 0
    step = 1
    while curr < n:
      if s[curr] in "()":
        curr = pair[curr]
        step = -step
      else:
        res.append(s[curr])
      curr += step
    return "".join(res)