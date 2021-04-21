class Solution:
    def minOperations(self, n: int) -> int:
        
        step = 0
        y = 0
        x = n - 1
        while y <= x:
            a =  (x * 2) + 1
            step += abs(n - a)
            y += 1
            x -= 1
        return step
                
        
