/*
Problem Decription:
  
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:
  Input: strs = ["flower","flow","flight"]
  Output: "fl" 

*/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
  
        i = 0
        for i, char in enumerate(strs[0]):          
            value = char
            for word in strs:
                if len(word)>i and word[i] == value:
                    # max_index = max_index + 1
                    continue
                else:
                    # max_index = i
                    return strs[0][:i]
            # max_index = i
            # print(max_index)
        return strs[0][:i+1]         
        
    
