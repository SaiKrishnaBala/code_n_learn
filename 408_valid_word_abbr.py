# Valid Word Abbrevation
# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        index2 = 0
        index1 = 0
        word_len = len(word)
        while index1 < len(abbr):
            if not abbr[index1].isdigit():
                if abbr[index1] != word[index2]:
                    return False
                else:
                    index2 += 1
                    index1 += 1
            else:
                prev_res = 0
                if int(abbr[index1]) == 0:
                    return False
                while index1 < len(abbr):
                    if abbr[index1].isdigit():
                        curr_num = int(abbr[index1])
                        prev_res = 10*prev_res + curr_num
                        index1 += 1
                    else:
                        break
                index2 += prev_res
            if index1 == len(abbr):
                if (index2 == word_len):
                    return True
                else:
                    return False
            else:
                if index2 >= word_len:
                    return False
        
