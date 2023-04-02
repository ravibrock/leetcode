class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        letter = 0
        final = []
        final_list = []
        while letter < len(s):
            if s[letter] not in final:
                final.append(s[letter])
                final_list.append(len(final))
                letter += 1
            else:
                final = final[1:]
        
        return max(final_list)
