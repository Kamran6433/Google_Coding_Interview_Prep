# You are given a string that represents time in the format hh:mm. 
# Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is
# the maximum possible.

# Maximum time: 23:59 
# Minimum time: 00:00

# You can assume the input string is always valid.

def maxTime(s):
    s=list(s)
    if s[0] == '?':
        s[0] = '2' if s[1] <= '3' or s[1] == '?' else '1'
    if s[1]=='?': s[1]='9' if s[0]!='2' else '3'
    if s[3]=='?': s[3]='5'
    if s[4]=='?': s[4]='9'
    return ''.join(s)
    
