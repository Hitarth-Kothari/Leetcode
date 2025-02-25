class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = 0
        check = 0
        while i + check < len(s):
            if s[i + check] != part[check]:
                i += 1
                check = 0
            else:
                check += 1
            if check == len(part):
                print(s[:i]+s[i+check:])
                return self.removeOccurrences(s[:i]+s[i+check:], part)
        return s
