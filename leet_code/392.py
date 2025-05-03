def isSubsequence(s: str, t: str) -> bool:
    p1 = 0
    p2 = 0

    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            p1 += 1
        p2 += 1

    return p1 == len(s)


print(isSubsequence(s="abc", t="ahbgdc"))


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
