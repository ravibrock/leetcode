class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       queue, solutions = collections.deque(), []
       for n in candidates: queue.append((target - n, [n]))
       while queue:
           node = queue.pop()
           if node[0] == 0: solutions.append(node[1])
           elif node[0] > 0:
               for n in candidates: queue.append((node[0] - n, node[1] + [n]))
       
       clean_sol = []
       for solution in solutions:
           sort = sorted(solution)
           if sort not in clean_sol: clean_sol.append(sort)
       return clean_sol
