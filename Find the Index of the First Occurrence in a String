class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        hay_len = len(haystack)
        needle_len = len(needle)
        while i + j < hay_len:
            if haystack[i+j] == needle[j]:
                j += 1
            else:
                i += 1
                j = 0
            if j == needle_len:
                return i
        return -1
