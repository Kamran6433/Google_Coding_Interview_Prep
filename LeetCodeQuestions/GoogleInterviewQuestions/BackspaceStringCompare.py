# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        stack1 = []
        stack2 = []
        for i in s:
            if not i == "#":
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
                else:
                    continue
        
        for j in t:
            if not j == "#":
                stack2.append(j)
            else:
                if stack2:
                    stack2.pop()
                else:
                    continue
                
        return stack1 == stack2