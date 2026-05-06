class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        l,r = 0,0
        window_dup = set()
        cur_max = 0
        while r < len(s):
            can_grow = s[r] not in window_dup
            if can_grow:
                window_dup.add(s[r])
                r += 1
                cur_max = max(cur_max, r-l)
            else:
                window_dup.remove(s[l])
                l += 1
            

        return cur_max