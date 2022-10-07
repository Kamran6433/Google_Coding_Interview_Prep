# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(sekf, s: str) -> int:
        answer = 0
        l = 0

        for i in range(len(s)):
            if len(s[l:i+1]) == len(set(s[l:i+1])):
                answer = max(answer, i-l+1)
            else:
                l += 1

        return answer