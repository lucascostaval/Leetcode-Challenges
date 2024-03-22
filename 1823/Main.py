class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1: return n
        friends = list(range(n))
        start_index = k-1
        removed = 0
        while True:
            last_removed = -1
            removed_now = 0
            for i in range(start_index, len(friends), k):
                friends[i] = -1
                last_removed = i
                removed_now += 1
                removed += 1
                if removed == n-1: break
            start_index = last_removed-removed_now
            removed_now = 0
            for i in range(len(friends)):
                if friends[i] == -1: removed_now += 1
                else: friends[i-removed_now] = friends[i]
            for _ in range(removed_now): friends.pop()
            start_index = (start_index+k)%len(friends)
            if removed == n-1: break
        return friends.pop()+1
            

sol = Solution()
n = 6
k = 5
print(sol.findTheWinner(n, k))