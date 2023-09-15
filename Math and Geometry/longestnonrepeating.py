class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        window_size = 0
        max_size = 0

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[i - window_size])
                window_size -= 1
            window.add(s[i])
            window_size += 1
            max_size = max(max_size, window_size)

        return max_size


sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))
