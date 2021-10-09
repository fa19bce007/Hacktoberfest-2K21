/*
Problem Description

Longest Substring Without Repeating Characters

Ex.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

*/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        slow = 0
        for i in range(1, len(s)):
            if s[i] in s[slow : i]:
                slow = s[slow:i].index(s[i]) + slow + 1
                #print(slow)
            res = max(res, i - slow + 1)
        return res
