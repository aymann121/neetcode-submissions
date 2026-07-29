class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        if len(s) == 0:
            return [[]]

        def isPalindrome(string):
            p1, p2 = 0, len(string)-1
            while p1 < p2:
                if string[p1] != string[p2]:
                    return False
                p1 += 1
                p2 -= 1
            return True

        firstPart = 1
        res = []
        while firstPart <= len(s):
            # print(res)
            if isPalindrome(s[0:firstPart]):
                rest = self.partition(s[firstPart:])
                for e in rest:
                    e.insert(0,s[0:firstPart])
                    res.append(e)
            firstPart +=1
        # print(res)
        return res