from typing import List
from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0

        def dfs(node):
            nonlocal count
            visited[node] = True
            total = values[node]

            for nei in graph[node]:
                if not visited[nei]:
                    total += dfs(nei)

            # If total sum divisible by k, form a component
            if total % k == 0:
                count += 1
                return 0  # break the component here

            return total

        dfs(0)
        return count


# ----------------- MAIN TEST AREA ------------------

if __name__ == "__main__":
    obj = Solution()

nums = [3, 9, 7]
edges = [[0, 1], [1, 2]]
k = 5


result = obj.maxKDivisibleComponents(3, edges, nums, k)
print("Output:", result)
