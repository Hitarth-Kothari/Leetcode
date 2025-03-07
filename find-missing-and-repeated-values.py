class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        S = 0
        P = 0
        SS = 0
        PP = 0
        for i in range(n*n+1):
            S += i
            P += i*i
        for i in range(n):
            for j in range(n):
                SS += grid[i][j]
                PP += grid[i][j]*grid[i][j]
        a_minus_b = SS - S
        a_plus_b = (PP-P)/(SS - S)
        a = (a_minus_b + a_plus_b)/2
        b = a_plus_b - a
        print(S, P, SS, PP)
        return [int(a), int(b)]
        
