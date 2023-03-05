'''
https://leetcode.com/problems/jump-game-iv/'
[solution needs improvement]
'''

class Solution:
    def minJumps(self, arr: List[int]) -> int:

        n = len(arr)

        if n == 1:
            return 0

        if arr[0] == arr[-1]:
            return 1
        
        val_map = {}
        visited = {}
        for i,v in enumerate(arr):
            if v not in val_map:
                val_map[v] = []
            if v not in visited:
                visited[v] = 0
            if i>0 and i<n-1 and arr[i-1] == v and arr[i+1] == v:
                continue
            val_map[v].append(i)

        if len([x for x in val_map.values() if len(x) > 1]) == 0:
            return n-1

        visited[arr[0]] += 1
        queue = [0]

        steps = 0
        while queue:
            size = len(queue)
            temp_steps = steps
            while size > 0:
                size -= 1
                i = queue.pop(0)
                if n - 1 == i:
                    return steps
                adj = set()
                adj.update(val_map[arr[i]])
                adj.update([i+1, i-1])
                for j in sorted(list(adj), reverse = True):
                    if j >= 0 and j < n and visited[arr[j]] < 8:
                        queue.append(j)
                        visited[arr[j]] +=1
            steps += 1
        
