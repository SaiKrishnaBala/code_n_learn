# 22 Generate Paranthesis
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        
        def backtrack(curr_ans, left, right):
            if len(curr_ans) == 2*n:
                ans.append("".join(curr_ans))
                return
            if left < n:
                curr_ans.append('(')
                backtrack(curr_ans, left+1, right)
                curr_ans.pop()
            if right < left:
                curr_ans.append(')')
                backtrack(curr_ans, left, right+1)
                curr_ans.pop()
                
        backtrack([], 0, 0)
        return ans
