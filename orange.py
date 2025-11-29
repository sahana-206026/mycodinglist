from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        # Step 1: Add all rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1

        # Directions: up, down, left, right
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        time = 0
        
        # Step 2: BFS processing
        while q:
            r, c, time = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and fresh orange
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # make it rotten
                    fresh -= 1
                    q.append((nr, nc, time + 1))  # add new rotten orange
        
        # Step 3: If fresh oranges still exist → impossible
        return time if fresh == 0 else -1


# ------------------- Test Code -------------------
if __name__ == "__main__":
    obj = Solution()
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    print(obj.orangesRotting(grid))
