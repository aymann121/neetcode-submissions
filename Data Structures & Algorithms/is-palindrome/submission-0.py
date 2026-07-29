class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) -1

        while ( leftPointer < rightPointer):
            while not s[leftPointer].isalnum() and leftPointer < rightPointer:
                leftPointer += 1
            while not s[rightPointer].isalnum() and leftPointer < rightPointer:
                rightPointer -= 1
            if s[rightPointer].lower() != s[leftPointer].lower():
                return False
            rightPointer -= 1
            leftPointer += 1
        return True
                

