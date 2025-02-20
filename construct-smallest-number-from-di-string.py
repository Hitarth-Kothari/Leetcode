class Solution:
    def smallestNumber(self, pattern: str) -> str:
        sol = list("123456789")
        sol = sol[:len(pattern)+1]
        switches = []
        
        for i in range(len(pattern)):
            if pattern[i] == "D":
                if not switches:
                    switches.append([i, i])
                elif switches[-1][1] == i - 1:
                    switches[-1][1] = i
                else:
                    switches.append([i, i])
        
        for start, end in switches:
            sol[start:end+2] = sol[start:end+2][::-1]
    
        return "".join(sol)
