# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        stack = []
        
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack)==0:
                    stack.append(i)
                    break
                if i == ")" and stack[-1] == "(":
                    stack.pop()

                elif i == "}" and stack[-1] == "{":
                    stack.pop()

                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    break
            

        if len(stack)>0:
            return False
        else:
            return True