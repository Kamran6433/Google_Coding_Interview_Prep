# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):

        if(x < 0 or (x % 10 == 0 and x != 0)):
            return False

        revertedNumber = 0
        while (x > revertedNumber):
            revertedNumber = revertedNumber * 10 + x % 10
            x /= 10

        return x == revertedNumber or x == revertedNumber/10

        
# faster solution:
class Solution(object):
    def isPalindrome(self, x):
      return str(x) == str(x)[::-1]