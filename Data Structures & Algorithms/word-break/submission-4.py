class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        memo = {}
        def helper(string):
            if string in memo: return memo[string]
            if string == "": return True
            p1 = 1
            valid = False
            while p1 <= len(string):
                if string[:p1] in wordSet:
                    valid = valid or helper(string[p1:])
                p1 += 1
            memo[string] = valid
            return valid

        return helper(s)