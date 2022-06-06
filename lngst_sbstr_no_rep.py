// Longest Substring Without Repeating Characters
// Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        i = 0
        curr_max = 1
        seen_letters = defaultdict(int)
        seen_letters[s[i]] = 1
        for j in range(1, len(s)):
            if s[j] not in seen_letters.keys():
                seen_letters[s[j]] = 1
                curr_max = max(curr_max, j-i+1)
                print(curr_max, seen_letters.keys())
            else:
                while(i <= j-1):
                    del seen_letters[s[i]]
                    if s[i] == s[j]:
                        i += 1
                        break
                    i += 1
                seen_letters[s[j]] += 1
        return curr_max
