"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
A string s is said to be one distance apart from a string t if you can:
Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
________________________________________________________________________________________________________________________
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
________________________________________________________________________________________________________________________
Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
===========================================LEARNINGS====================================================================
"""
S = "a"
T = "ac"

def isOneEditDistance(s: str, t: str) -> bool:
    if len(t) < len(s): s, t = t, s
    s_len, t_len = len(s), len(t)
    if t_len - s_len > 1: return False
    edit = False
    print("--------->",s)
    print("--------->",t)
    if s_len == t_len:
        if s == t : return False
        for i in range(s_len):
            if s[i] != t[i] and edit is not True:
                edit = True
            elif s[i] != t[i] and edit is True:
                return False
    elif s_len + 1 == t_len:

        up, down = 0, 0
        while up < s_len != 0 and down < t_len:
            if s[up] == t[down]:
                up, down = up + 1, down + 1
            elif s[up] != t[down] and edit is not True:
                edit = True
                down += 1
            elif s[up] != t[down] and edit is True:
                return False
    return True






print(isOneEditDistance(S,T))

# ======================================================================================================================
# Instead of using the Edit variable smarter way is to check substring from the point of difference
class Solution:
    def isOneEditDistance(self, s: 'str', t: 'str') -> 'bool':
        ns, nt = len(s), len(t)
        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        return ns + 1 == nt

